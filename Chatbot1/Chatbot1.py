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
# Sunday: 3 hours
# Monday


# Importing necessary libraries
from textblob import TextBlob

# Dictionary to store user profiles
user_profiles = {}

class UserProfile:
    def __init__(self, name, age, username, email):
        self.name = name
        self.age = age
        self.username = username
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nUsername: {self.username}\nEmail: {self.email}"

class StudentProfile(UserProfile):
    def __init__(self, name, age, username, email, student_id, courses):
        super().__init__(name, age, username, email)
        self.student_id = student_id
        self.courses = courses

    def __str__(self):
        return super().__str__() + f"\nStudent ID: {self.student_id}\nCourses: {', '.join(self.courses)}"

# Defining the GuestProfile class that inherits from UserProfile
class GuestProfile(UserProfile):
    def __init__(self, name, age, username, email, guest_type):
        super().__init__(name, age, username, email)
        self.guest_type = guest_type

    def __str__(self):
        return super().__str__() + f"\nGuest Type: {self.guest_type}"

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

# Function to create a new user profile
def create_user_profile():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    username = input("Enter username: ")
    email = input("Enter email: ")
    user_profile = UserProfile(name, age, username, email)
    
    # Write user information to a file
    with open(r"F:\AI School\MS Adv Prog\Chatbot1\user_profile.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Email: {email}\n")
        

    return UserProfile(name, age, username, email)

# Function to create a new student profile
def create_student_profile():
    user_profile = create_user_profile()
    student_id = input("Enter student ID: ")
    num_courses = int(input("Enter number of courses: "))
    courses = []
    for _ in range(num_courses):
        course = input("Enter course name: ")
        courses.append(course)
    student_profile = StudentProfile(user_profile.name, user_profile.age, user_profile.username, user_profile.email, student_id, courses)
    return student_profile

# Function to create a new guest profile
def create_guest_profile():
    user_profile = create_user_profile()
    guest_type = input("Enter guest type: ")
    guest_profile = GuestProfile(user_profile.name, user_profile.age, user_profile.username, user_profile.email, guest_type)
    return guest_profile

# Append user profile to file
def append_to_file(profile, file_path):
    with open(file_path, "a") as file:
        file.write(str(profile) + "\n\n")

# Append user profile to dictionary
def append_to_dict(profile_dict, profile):
    profile_dict[profile.username] = profile

# Example usage
student_profile = create_student_profile()
append_to_file(student_profile, "user_profile.txt")
append_to_dict(user_profiles, student_profile)

guest_profile = create_guest_profile()
append_to_file(guest_profile, "user_profile.txt")
append_to_dict(user_profiles, guest_profile)

# Print user profiles
for username, profile in user_profiles.items():
    print(f"Username: {username}")
    print(profile)
    print()

if __name__ == "__main__":
    main()
