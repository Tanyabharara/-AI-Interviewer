from models.llm_loader import get_llm


def evaluate_answer(question, answer):
    llm = get_llm()
    prompt = f"Question: {question}\nCandidate's answer: {answer}\nEvaluate the answer. Is it correct, partially correct, or incorrect? Give a score (0-2) and a short explanation. If the answer is weak, suggest a follow-up question or hint. Respond in JSON: {{\"score\": ..., \"explanation\": ..., \"followup\": ...}}"
    response = llm.invoke(prompt)
    # You may want to parse the JSON here in production
    return response.strip() 