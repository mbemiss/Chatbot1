# Estimated time: 3.5 hours
# Sunday: 2 hours
# Monday: 2 hours
# Tuesday: 1 hour
# Total: 5 hours
# 
# Extra time taken to add sentiment analysis and troubleshoot why lowercase "exit" and uppercase "EXIT"
# were behaving the same.

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
        # Analyze the sentiment of the user's input
        sentiment = processed_input.sentiment
        sentiment_value = f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}"
        if sentiment.polarity > 0:
            return f"That sounds positive! ({sentiment_value})"
        elif sentiment.polarity < 0:
            return f"That sounds negative. ({sentiment_value})"
        else:
            return f"That sounds neutral. ({sentiment_value})"

def main():
    print("Welcome to the Simple Chat Bot!")
    print("You can type 'exit' in lowercase to continue the conversation or 'EXIT' in uppercase to exit the conversation.")

    while True:
        try:
            user_input = input("You: ")
            if not user_input.strip():
                print("Chat Bot: Please enter a valid input.")
                continue

            if user_input == "exit":
                print("Chat Bot: You typed 'exit' in lowercase. Continuing the conversation.")
                continue
            elif user_input.upper() == "EXIT":
                print("Chat Bot: Goodbye!")
                break
            
            if user_input == "menu":
                print("Chat Bot: You typed 'menu' in lowercase. Continuing the conversation.")
                continue
            elif user_input.upper() == "MENU":
                print("Chat Bot: Restarting the conversation.")
                # Add code here to reset any necessary variables for conversation restart
                print("Welcome to the Simple Chat Bot!")
                continue

            processed_input = process_input(user_input)
            intent = identify_intent(processed_input)
            response = generate_response(processed_input, intent)

            print("Chat Bot:", response)
        except Exception as e:
            print("Chat Bot: An error occurred:", e)

if __name__ == "__main__":
    main()


