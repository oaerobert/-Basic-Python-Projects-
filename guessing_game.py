# Number Guessing Game
# The program selects a random number, and the user has three chances to guess it.
import random
# Initialise variables
guess_count = 0
guess_limit = 3
secret_number = random.randint(1,10)

while guess_count < guess_limit:
    try:
        # User input
        guess = int(input(f"I have randomly selected a number between 1 and 10. Take a guess what you think it is: "))
        # Increment guess count
        guess_count +=1
        if guess == secret_number:
            print(f"Well done, you guessed correctly! ")
            break
        elif guess != secret_number:
            remaining_guesses = guess_limit - guess_count
            if remaining_guesses > 1:
                print(f"You have {remaining_guesses} guesses left. Please try again.")
            if remaining_guesses == 1:
                print(f"You have one try left. Please try again.")
    except ValueError:
        print(f"Invalid Input. Please enter a valid number.")

if guess_count == guess_limit:
    print(f"Unfortunately, you have exhausted all your tries. The correct number was {secret_number}")