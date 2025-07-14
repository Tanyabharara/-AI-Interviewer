class MemoryManager:
    def __init__(self):
        self.state = {
            'topic': None,
            'questions': [],
            'answers': [],
            'scores': [],
            'current_question': 0,
            'feedback': None
        }

    def set_topic(self, topic):
        self.state['topic'] = topic

    def add_question(self, question):
        self.state['questions'].append(question)

    def add_answer(self, answer):
        self.state['answers'].append(answer)

    def add_score(self, score):
        self.state['scores'].append(score)

    def set_feedback(self, feedback):
        self.state['feedback'] = feedback

    def next_question(self):
        self.state['current_question'] += 1

    def get_state(self):
        return self.state 