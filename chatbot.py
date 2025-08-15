import random
from datetime import datetime
print("Hello! I am ChatBot 🤖. Type 'bye' to exit.")
print("You can say 'hi,hello,hey','how are yoy','your name','time','date','joke','weather','bye'")
jokes = [
    "Why don’t skeletons fight each other? Because they don’t have the guts!",
    "What do you call fake spaghetti? An Impasta!",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why was the math book sad? It had too many problems."
]
while True:
    user_input = input("You: ").lower()
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello there! How’s your day going?")
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking. 😊 How about you?")
    elif "your name" in user_input:
        print("Bot: I’m ChatBot, your friendly assistant.")
    elif "time" in user_input:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: The current time is {now}.")
    elif "date" in user_input:
        today = datetime.now().strftime("%Y-%m-%d")
        print(f"Bot: Today’s date is {today}.")
    elif "joke" in user_input:
        print(f"Bot: {random.choice(jokes)} ")
    elif "weather" in user_input:
        print("Bot: I can't check live weather yet, but I can guess it’s sunny somewhere!")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a wonderful day!")
        break
    else:
        print("Bot: Hmm, I don’t know how to respond to that. Try asking me for a joke or the time!")