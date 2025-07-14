from langgraph_app.graph import build_interview_graph, InterviewState
def main():
    print("Welcome to the AI Technical Interviewer!\n")
    topic = input("Enter the interview topic (e.g., JavaScript, Machine Learning): ")
    compiled_graph, memory = build_interview_graph()
    memory.set_topic(topic)

    # Initialize state
    state = {
        'topic': topic,
        'answers': [],
        'question': '',
        'eval_result': {},
        'summarize': False
    }  # type: InterviewState

    num_questions = 3  # You can make this configurable
    for i in range(num_questions):
        state = compiled_graph.invoke(state)

    # Summarize at the end
    state['summarize'] = True
    compiled_graph.invoke(state)

if __name__ == "__main__":
    main() 