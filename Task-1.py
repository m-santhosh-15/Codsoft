from datetime import datetime 

def chatbot_response(user_input):
    user_input = user_input.lower()
    # Predefined responses based on user 
    if "hello" in user_input or "hi" in user_input:
        user_input = user_input.capitalize()
        return f"{user_input}! What is your name?"
    elif "what is the time" in user_input or "time" in user_input:
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"Now the  time is {current_time}"
    elif "what is the date" in user_input or "date" in user_input:
        current_date = datetime.today().strftime("%d-%b-%Y")
        return f"Today's date is {current_date}"
    elif "my name is" in user_input or "" in user_input:
        name = user_input.split("my name is")[-1].strip().title()
        return f"Nice to meet you, {name}! How can I help you today?"
    elif "what is your name" in user_input:
        return "I am your friendly chatbot. What's your name?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"




# Main loop 
print("Welcome to the simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        print("Chatbot:", chatbot_response(user_input))
