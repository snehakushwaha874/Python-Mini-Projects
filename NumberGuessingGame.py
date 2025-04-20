import random
number_to_guess = random.randint(1,10)
guess = None
attempts = 0

print("Welcome to the number guessing game !")
print("Thinking of number between 1 to 10")

while guess!=number_to_guess:
    guess=int(input("Enter your guess : "))
    attempts += 1

    if guess < number_to_guess:
        print("Too less! Try again")
    elif guess > number_to_guess:
        print("Too more! Try again")
    else:
        print(f"Congratulations! You guessed it in {attempts} tries.)")