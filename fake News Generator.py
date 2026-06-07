import random

#list of Subjects 
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

#List of Actions 
actions= [
    "Launches",
    "canclels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

#List of Places and things 
places_or_things=[
    "at red fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

#while repeat a program or generate fake news untile the user said no.
while True:
    subject = random.choice(subjects)   #randomly choses subject from subjects list 
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)
    
    
    #concatinate the subject, action and place or things and make headlines.
    headline = f"BREAKING NEWS: {subject} {action} {places_or_thing}"
    print("\n" + headline)
    
    user_input=input("\n Do you want another headline? (yes/no): ").lower()
    if user_input=="no":   #when user say no it will stop 
        break
    
print("\n Thanks for using the Fake News Headline Generator. Have a fun day.")