#generate random number
import random

num_to_guess=random.randint(1,100)
while True:
    try: 
        guess=int(input("enter the guess(1-100):"))
        if guess<num_to_guess:
            print("Too Low!")
        elif guess>num_to_guess:
            print("Too High!")
        else:
            print('Congratulations! You guess write number.')
            break
    except ValueError:
        print("Please enter valid Number.")

