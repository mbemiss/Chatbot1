# Project 1
# Estimated time: 3.5 hours
# Sunday: 2 hours
# Monday: 2 hours
# Tuesday: 1 hour
# Total: 5 hours
# 
# Extra time taken to add sentiment analysis and troubleshoot why lowercase "exit" and uppercase "EXIT"
# were behaving the same.
#
# Project 2
# Estimated time: 4 hours
# Sunday: 



from textblob import TextBlob

class UserProfile:
    def __init__(self, name, age, preferences):
        self.name = name
        self.age = age
        self.preferences = preferences

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Preferences: {self.preferences}"

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
        response = "I'm sorry, I'm just a simple chat bot and I can't answer questions."
    else:
        # Analyze the sentiment of the user's input
        sentiment = processed_input.sentiment
        sentiment_value = f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}"
        if sentiment.polarity > 0:
            response = f"That sounds positive! ({sentiment_value})"
        elif sentiment.polarity < 0:
            response = f"That sounds negative. ({sentiment_value})"
        else:
            response = f"That sounds neutral. ({sentiment_value})"

    return response

def main():
    print("Welcome to the Simple Chat Bot!")
    print("You can type 'exit' in lowercase to continue the conversation or 'EXIT' in uppercase to exit the conversation.")

    # Create a new user profile
    user_profile = create_user_profile()

    while True:
        try:
            with open(r"F:\AI School\MS Adv Prog\Chatbot1\conversation_log.txt", "a") as file:            
                user_input = input("You: ")
                if not user_input.strip():
                    print("Chat Bot: Please enter a valid input.")
                    file.write(f"You: {user_input}\n")
                    file.write(f"Chat Bot: {response}\n\n")
                    continue

                if user_input == "exit":
                    print("Chat Bot: You typed 'exit' in lowercase. Continuing the conversation.")
                    file.write(f"You: {user_input}\n")
                    file.write(f"Chat Bot: {response}\n\n")
                    continue
                elif user_input.upper() == "EXIT":
                    file.write(f"You: {user_input}\n")
                    file.write(f"Chat Bot: {response}\n\n")
                    print("Chat Bot: Goodbye!")
                    break
            
                if user_input == "menu":
                    print("Chat Bot: You typed 'menu' in lowercase. Continuing the conversation.")
                    file.write(f"You: {user_input}\n")
                    file.write(f"Chat Bot: {response}\n\n")
                    continue
                elif user_input.upper() == "MENU":
                    print("Chat Bot: Restarting the conversation.")
                    file.write(f"You: {user_input}\n")
                    file.write(f"Chat Bot: {response}\n\n")
                    # Add code here to reset any necessary variables for conversation restart
                    print("Welcome to the Simple Chat Bot!")
                    file.write(f"Chat Bot: {response}\n\n")
                    continue

                processed_input = process_input(user_input)
                intent = identify_intent(processed_input)
                response = generate_response(processed_input, intent)

                # Print the response
                if response:
                    print("Chat Bot: ", response)
                    file.write(f"You: {user_input}\n")
                    file.write(f"Chat Bot: {response}\n\n")
        except Exception as e:
            print("Chat Bot: An error occurred:", e)

def create_user_profile():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    preferences = {}

    # Input preferences
    while True:
        preference = input("Enter a preference (or type 'done' to finish): ")
        if preference.lower() == 'done':
            break
        value = input(f"Enter a value for '{preference}': ")
        preferences[preference] = value

    # Write user information to a file
    with open(r"F:\AI School\MS Adv Prog\Chatbot1\user_profile.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write("Preferences:\n")
        for preference, value in preferences.items():
            file.write(f"{preference}: {value}\n")

    return UserProfile(name, age, preferences)

if __name__ == "__main__":
    main()
