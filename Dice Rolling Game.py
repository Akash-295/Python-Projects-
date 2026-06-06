#Ask: roll the dice?
import random
#loop
while True:  #repeating the choice
    choice= input("Roll the dice? (y/n): ").lower()
    if choice =='y':   #if user say yes(y)
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")

    elif choice =='n':   #if user say no 'n'
        print("Thanks for playing!")
        break
    else:
        print("invalid choice!")
    
#print thank you message
#terminate
#else
#print invalid choice