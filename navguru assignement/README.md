<<<<<<< HEAD
# AI Interviewer

An AI-powered technical interviewer CLI app using LangGraph and OpenAI (or local LLMs).

## Features
- Simulates a technical interview with 3-5 dynamic questions
- Branching logic: follow-ups and hints based on your answers
- Summarizes your performance and gives feedback
- Modular, extensible design

## Setup
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


   ```

## Usage
```bash
python app/main.py
```

## Project Structure
- `app/`: CLI interface
- `langgraph_app/`: Interview flow and nodes
- `models/`: LLM loader
- `memory/`: Conversation state
- `prompts/`: Prompt templates

## Technologies
- LangGraph
- LangChain
- OpenAI (or local LLMs)

## Design
- Each interview step is a node in a LangGraph graph
- Branching logic for follow-ups and hints
- Easy to extend with new topics or LLMs

--- 
=======
# -AI-Interviewer
>>>>>>> 5cbaa76632319b56061f6ec383f48d936739c863
