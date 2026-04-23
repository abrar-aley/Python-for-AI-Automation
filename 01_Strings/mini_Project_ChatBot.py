# mini project ChatBot

while True:
    chat= input('You: ').lower()
    if chat== 'hi':
        print('Bot: Hello!')
    elif chat== 'how are you':
        print("Bot: I am fine")
    elif chat== 'bye':
        print('Bot: Good Bye')
        break
    else:
        print('Bot: I didnt understand')