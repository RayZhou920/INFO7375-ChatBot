# info7375-chatbot

### Youtube video link

https://youtu.be/zRxHK9UWJg8

### Setup Process

- Navigate to the current directory in your command line.
1. `python3 -m venv .venv` - Create a Python virtual environment
2. `source .venv/bin/activate` - Activate the virtual environment
3. `pip install -r requirements.txt` - Install all required packages
4. `streamlit run chatbot.py` - Start the chatbot, which will automatically open in your browser
5. `deactivate`- When you are done using the chatbot, deactivate the virtual environment

### Domain selection

- User Base: This chatbot serves patients and the general public who seek general health information and preventive care advice.
- Scope of Queries:
  - General health inquiries (excluding diagnosis).
  - Information about medical tests and procedures.

### Unique features

1. The chatbot will not respond to non-health-related questions and will provide users with an error message.
2. It includes a list of sample questions to assist beginners.
3. The conversation is styled for a clearer and more structured interaction.
4. It retains the context of the current conversation until explicitly cleared by the user.

### Technology Stacks

1. Python: Streamlit is used as the frontend framework.
2. Python: NLTK (Natural Language Toolkit) is employed to identify popular health query keywords.
3. Machine Learning: Utilizes the Ollama/Llama3 large language model (LLM).
