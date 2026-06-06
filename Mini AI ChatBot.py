#Rule Based Chat Bot Assistant.

import datetime

presenthour= datetime.datetime.now().hour
name=input("enter your name: ")

if 5<=presenthour<=12:
    print("Good Morning,",name)
elif 12<=presenthour<=17:
    print("Good afternoon,",name)
elif 17<=presenthour<=20:
    print("Good Evening,",name)
else:
    print("Good night,",name)



print("Welcome to Rule Based ChatBot😄.")
print("You can ask me basic Question, Type 'Bye' to exit from the bot.")

#chatbot Memory Creation [Dictionary of responses]
responses={
    "hello": "Hi, welcome. How can I Help You?",
    "how are you":"I am very fine. Thank You.",
    "Who are you":"I am smart AI chatbot.",
    "motivate me":"Keep going. Every bug of your project makes you a best.",
    "happy":"Great to hear that",
    "what is function": "I need to learn or read that before response you."
}


#Method/Function to get response of ChatBoat

def GetResponseOfBoat(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "I am not able to answer that yet. I am still in learning mode."


#take user input
while True:
    userInput=input("You: ")

    if  userInput.lower()=="bye":
        print("Bot: GoodBye! Have a great day.😊")
        break
    
    reply=GetResponseOfBoat(userInput)
    print("Bot👀: ", reply)

    
