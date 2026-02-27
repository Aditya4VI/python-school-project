print("ChatBot Started (type 'bye' to exit)")

bot_data1 = ["hi", "hello", "hey"]
bot_data2 = ["bye"]
bot_data3 = ["how are you", "are you fine"]
bot_data4 = ["i am fine", "i am happy"]
bot_data5 = ["i am not happy", "i am sad"]

while True:
    user = input("You: ").lower()

    if any(word in user for word in bot_data1):
        print("Bot: Hey! Welcome to you. ")

    elif any(word in user for word in bot_data3):
        print("Bot: I am fine bro. ")

    elif any(word in user for word in bot_data4):
        print("Bot: Nice to hear that you are fine. ")

    elif any(word in user for word in bot_data5):
        print("Bot: I feel sorry that you are sad. ")

    elif any(word in user for word in bot_data2):
        print("Bot: Nice to meet you, bye. ")
        break

    else:
        print("Bot: Sorry, I didn’t understand that. ")

i=input("Press Enter to exit.  ")