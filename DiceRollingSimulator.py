import random

def roll_dice():
    return random.randint(1,6)

print("Dice Rolling Simulator")

while True:
    roll=input("Roll the Dice? (yes/no) : ").lower()

    if roll == "yes":
        print("You Rolled : ",roll_dice())
    elif roll == "no":
        print("Thanks for playing !")
        break
    else:
        print("Please type 'yes' or 'no'")