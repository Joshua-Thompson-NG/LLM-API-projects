import sys
from pathlib import Path

# Ensure project root is in sys.path when running main.py directly
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.llm import create_chat_session

def main():
    print("=== Gemini CLI Chatbot (Type 'exit' or 'quit' to stop) ===")
    chat = create_chat_session(
        system_instruction="You are a helpful and concise AI assistant.",
    )

    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            response = chat.send_message(user_input)
            print("\nAI:", response.text)
        except KeyboardInterrupt:
            print("\nSession Ended!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()

