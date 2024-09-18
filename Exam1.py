# Importing randint from random library
from random import randint

# Prompt for the user's name
name = input("Hello! What is your name? ")

# Greet the user and explain the game
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("You have 5 tries to guess the number.")

# Have the computer generate a random number between 1 and 20
secret_number = randint(1, 20)

# Loop for 5 attempts
for guesses_taken in range(1, 6):
    # Prompt the user for a guess
    guess = int(input("Take a guess: "))
    
    # Check if the guess is too high, too low, or correct
    if guess > secret_number:
        print("Your guess is too high.")
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        # If the guess is correct
        print(f"Good job, {name}! You guessed the number in {guesses_taken} tries!")
        break  # End the game
else:
    # If the user did not guess the number in 5 tries
    print(f"Sorry, {name}. You've used all 5 guesses. The number I was thinking of was {secret_number}.")
