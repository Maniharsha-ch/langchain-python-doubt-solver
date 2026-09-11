import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found. Check your .env file."
    )

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=api_key
)

# Create prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful Python tutor.

Answer the following Python question clearly and simply.
Use examples when useful.
Assume the user is a beginner.

Question: {question}
"""
)

print("=" * 50)
print("       AI PYTHON DOUBT SOLVER")
print("=" * 50)
print("Ask Python questions. Type 'exit' to quit.\n")

while True:
    question = input("Enter your Python question: ")

    if question.strip().lower() == "exit":
        print("Thank you for using AI Python Doubt Solver!")
        break

    if not question.strip():
        print("Please enter a valid question.\n")
        continue

    try:
        # Format prompt
        formatted_prompt = prompt_template.format(
            question=question
        )

        # Generate AI response
        response = llm.invoke(formatted_prompt)

        print("\nAI Answer:")
        print(response.text)
        print("\n" + "-" * 50 + "\n")

    except Exception as e:
        print("\nSorry, something went wrong while generating the answer.")
        print("Please check your internet connection or API configuration.\n")