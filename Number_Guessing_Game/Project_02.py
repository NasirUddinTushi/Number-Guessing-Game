import random


# number guessing game
def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    # the correct number is guessed
    while True:
        try:
            # Take user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is too low, too high, or correct
            if user_guess < number_to_guess:
                print("Too low!")
            elif user_guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# start the game
number_guessing_game()
