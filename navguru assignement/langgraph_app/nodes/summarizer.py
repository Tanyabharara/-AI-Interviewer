from models.llm_loader import get_llm

FEEDBACK_PROMPT = open('prompts/feedback_prompt.txt').read()


def summarize_interview(questions, answers, scores):
    llm = get_llm()
    prompt = f"{FEEDBACK_PROMPT}\n\nQuestions: {questions}\nAnswers: {answers}\nScores: {scores}"
    response = llm.invoke(prompt)
    return response.strip() 