# info7375-chatbot

### Setup process

1. Head to current directory in your command line
2. `python3 -m venv .venv`
3. `source .venv/bin/activate` to activate a Python virtual environment
4. `pip install -r requirements.txt` to install all the packages
5. `streamlit run chatbot.py` and the chatbot will automatically start in your browser
6. After you finish checking the chatbot, type `deactivate` in your command line to exit the Python virtual environment

### Domain selection

- User Base: Patients and the general public looking for general health information, and preventive care advice.
- Scope of Queries:
  - General health questions (not for diagnosis).
  - Information about medical tests and procedures.

### Unique features

1. Questions regarding non-health topics will not be responded and give users an error message
2. List some sample questions for beginners
3. Style the conversation so that it has a clearer structure

### Stacks I used

1. Python - Streamlit as frontend framework
2. Python - nltk (Natural Language Processing with Python provides a practical introduction to programming for language processing) to get some popular health query keywords
3. ollama/llama3 LLM model

### Future improvements

1. In this assignment, I generate ~250 most popular health query keywords. And the chatbot will check if users' questions include one of the keywords. If no, then the question won't be responded.
   **Improvements**
   1. What if users have typos in their questions?
      Implement NLU (Natural Language Understanding) to grasp the context and the intent behind the user’s query, which can help in providing more accurate responses or in routing the query correctly.
   2. What if users ask a question that is health-related but there is no keywords matched?
      Use NER (Named Entity Recognition) to identify medical entities in the text, such as drug names, symptoms, or diseases.
2. The conversation doesn't feel like a real chat app.
   **Improvements**
   1. Explore more about Streamlit to know how to style it.
