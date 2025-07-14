from langgraph.graph import StateGraph
from langgraph.graph import END, START
from langgraph_app.nodes.question_generator import generate_question
from langgraph_app.nodes.answer_evaluator import evaluate_answer
from langgraph_app.nodes.followup_handler import handle_followup
from langgraph_app.nodes.summarizer import summarize_interview
from memory.memory_manager import MemoryManager
from typing import TypedDict, List, Dict
import json
import re


class InterviewState(TypedDict):
    topic: str
    answers: List[str]
    question: str
    eval_result: Dict
    summarize: bool


def build_interview_graph():
    memory = MemoryManager()
    g = StateGraph(InterviewState)

    def ask_question(state):
        topic = state['topic']
        previous_answers = state['answers']
        question = generate_question(topic, previous_answers)
        memory.add_question(question)
        return {'question': question}

    def get_answer(state):
        answer = input(f"\n{state['question']}\n> ")
        memory.add_answer(answer)
        return {'answer': answer}

    def evaluate(state):
        question = memory.state['questions'][-1]
        answer = memory.state['answers'][-1]
        eval_result = evaluate_answer(question, answer)
        try:
            eval_result_dict = json.loads(eval_result)
        except Exception:
            eval_result_dict = {"score": None, "explanation": eval_result, "followup": None}
        # Clean up explanation: remove code formatting, replace \n with newlines, use bullets for lists
        explanation = eval_result_dict.get("explanation", "")
        explanation = re.sub(r'`+', '', explanation)
        explanation = explanation.replace('\\n', '\n').replace('\n', '\n')
        # Use bullets for feedback if multiple points
        if '\n' in explanation:
            lines = [line.strip() for line in explanation.split('\n') if line.strip()]
            if len(lines) > 1:
                explanation = '\n'.join([f"• {line}" for line in lines])
            else:
                explanation = lines[0] if lines else explanation
        eval_result_dict["explanation"] = explanation
        print(f"\nEvaluation:\n{explanation}")
        memory.add_score(eval_result_dict)
        return {'eval_result': eval_result_dict}


    def followup(state):
        # In production, parse eval_result for followup
        followup = None
        if 'followup' in state['eval_result']:
            followup = state['eval_result']['followup']
        if followup:
            print(f"\nFollow-up: {followup}")
            return {'followup': followup}
        return {}

    def summarize(state):
        questions = memory.state['questions']
        answers = memory.state['answers']
        scores = memory.state['scores']
        summary = summarize_interview(questions, answers, scores)
        summary_clean = re.sub(r'`+', '', summary)
        summary_clean = summary_clean.replace('\\n', '\n').replace('\n', '\n')
        if '\n' in summary_clean:
            lines = [line.strip() for line in summary_clean.split('\n') if line.strip()]
            if len(lines) > 1:
                summary_clean = '\n'.join([f"• {line}" for line in lines])
            else:
                summary_clean = lines[0] if lines else summary_clean
        print(f"\nInterview Summary:\n{summary_clean}")
        memory.set_feedback(summary_clean)
        return {END: True}

    # Add nodes
    g.add_node('ask_question', ask_question)
    g.add_node('get_answer', get_answer)
    g.add_node('evaluate', evaluate)
    g.add_node('followup', followup)
    g.add_node('summarize', summarize)

    # Define flow
    g.add_edge(START, 'ask_question')  # Entry point
    g.add_edge('ask_question', 'get_answer')
    g.add_edge('get_answer', 'evaluate')
    g.add_edge('evaluate', 'followup')
    g.add_edge('followup', 'ask_question')  # Loop for next question or follow-up
    g.add_edge('ask_question', 'summarize')  # End after N questions
    g.add_edge('summarize', END)  # Exit point

    # Compile the graph
    compiled_graph = g.compile()
    
    return compiled_graph, memory 