# AI Python Doubt Solver using LangChain

## 1. Project Title

AI Python Doubt Solver using LangChain and Google Gemini

## 2. Objective

To develop a simple AI-powered chatbot that answers Python programming questions using LangChain, a prompt template, and Google's Gemini Large Language Model.

## 3. Problem Statement

Beginners often face difficulty understanding Python programming concepts and require quick, simple, and understandable explanations. This project provides an interactive chatbot that answers Python-related doubts in a beginner-friendly manner.

## 4. Technologies Used

- Python
- LangChain
- Google Gemini
- langchain-google-genai
- python-dotenv
- Git and GitHub
- VS Code

## 5. Features

- Accepts Python questions from the user
- Generates AI-based answers
- Uses LangChain PromptTemplate
- Supports multiple questions in one session
- Provides beginner-friendly explanations
- Handles empty input
- Includes basic error handling
- Uses `.env` for API key security
- Exit command to terminate the chatbot

## 6. System Workflow

```text
User enters a Python question
            ↓
PromptTemplate formats the question
            ↓
LangChain sends the prompt to Gemini
            ↓
Gemini processes the question
            ↓
AI-generated answer is returned
            ↓
Answer is displayed in the terminal
```

## 7. Implementation

The project uses the following major components:

### Environment Configuration

The Gemini API key is loaded securely from the `.env` file using `python-dotenv`.

### Language Model

Google Gemini is connected through LangChain's `ChatGoogleGenerativeAI` class.

### Prompt Template

A prompt template instructs the model to behave as a helpful Python tutor and explain concepts simply.

### User Interaction

The chatbot continuously accepts questions until the user enters `exit`.

## 8. Sample Questions Tested

1. What is a list in Python?
2. What is the difference between a list and a tuple?
3. Explain Python functions with an example.
4. What is a dictionary in Python?
5. What is the difference between `==` and `is` in Python?

## 9. Expected Output

The chatbot displays an AI-generated explanation for each Python question entered by the user.

## 10. Advantages

- Easy to use
- Beginner-friendly
- Quick responses
- Simple command-line interface
- Secure API key handling
- Can answer a wide range of Python questions

## 11. Future Enhancements

- Add Streamlit graphical interface
- Add conversation history
- Add Python code execution
- Add quiz mode
- Add topic-based learning
- Deploy as a web application
- Add voice input and output

## 12. Learning Outcomes

- Understanding of LangChain fundamentals
- Working with LLM APIs
- Creating prompt templates
- Handling environment variables
- Building AI-powered applications
- Using Git and GitHub
- Writing project documentation

## 13. GitHub Repository

https://github.com/Maniharsha-ch/langchain-python-doubt-solver

## 14. Conclusion

The AI Python Doubt Solver successfully demonstrates how LangChain can be integrated with Google Gemini to build a useful AI-powered educational chatbot. The project provides beginner-friendly Python explanations and establishes a foundation for developing more advanced AI applications.