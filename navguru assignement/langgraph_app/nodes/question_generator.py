from models.llm_loader import get_llm

SYSTEM_PROMPT = open('prompts/system_prompt.txt').read()


def generate_question(topic, previous_answers):
    llm = get_llm()
    prompt = f"{SYSTEM_PROMPT}\n\nTopic: {topic}\nPrevious answers: {previous_answers}\nAsk the next technical question."
    response = llm.invoke(prompt)
    return response.strip() 