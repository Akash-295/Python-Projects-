#Password Guessing Game and it is text based game 
import random

easy_words = ['apple', 'train', 'tiger', 'money', 'india']
medium_words= ['python', 'bottle', 'monkey', 'planet', 'laptop']
hard_words=['elephant', 'diamond', 'umbrella', 'computer', 'mountains']

print("Welcome to the Password Guessing game.")
print("Choose a difficulty Level: easy, medium or hard.")

level = input("Enter Difficulty: ").lower()
if level == "easy":
    secret=random.choice(easy_words)
elif level == 'medium':
    secret = random.choice(medium_words)
elif level == 'hard':
    secret = random.choice(hard_words)
else:
    print("Invalid Choice. Defauling to easy level.")
    secret = random.choice(easy_words)
    
attempts = 0
print("\n Guess the Secret Password")

while True:
    guess = input("Enter you Guess: ").lower()
    attempts +=1
    if guess == secret:
        print(f"Congratulations! You guess it in {attempts} attempts.")
        break
    
    hint = ""
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint += guess[i]
        else:
            hint +="_"
            
    print("Hint: ", hint)
print("Game Over.")