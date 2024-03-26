from textblob import TextBlob

def process_input(user_input):
    # Use textblob to process the user's input
    processed_input = TextBlob(user_input)
    return processed_input

def identify_intent(processed_input):
    # Use textblob's capabilities to identify the user's intent
    # For simplicity, let's assume the intent is based on the type of question asked
    if processed_input.endswith("?"):
        return "question"
    else:
        return "statement"

def generate_response(processed_input, intent):
    # Generate an appropriate response based on the user's input and identified intent
    if intent == "question":
        return "I'm sorry, I'm just a simple chat bot and I can't answer questions."
    else:
        return "That's interesting!"

def main():
    print("Welcome to the Simple Chat Bot!")
    print("You can type 'exit' in lowercase to continue the conversation or 'EXIT' in uppercase to exit the conversation.")

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            print("Chat Bot: You typed 'exit' in lowercase. Continuing the conversation.")
            continue
        elif user_input.upper() == "EXIT":
            print("Chat Bot: Goodbye!")
            break

        processed_input = process_input(user_input)
        intent = identify_intent(processed_input)
        response = generate_response(processed_input, intent)

        print("Chat Bot:", response)

if __name__ == "__main__":
    main()

