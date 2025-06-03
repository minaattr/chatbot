
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

# Set your OpenAI API key from environment variable (recommended)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY environment variable.")

# Initialize the OpenAI LLM model
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# Memory to store conversation history
memory = ConversationBufferMemory()

# Create the conversational chain
conversation = ConversationChain(llm=llm, memory=memory)

def chat():
    print("🤖 Chatbot ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = conversation.run(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
