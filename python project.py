import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")
    
    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            
            # Increment the attempts
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
                print(secret_number)
                break
            elif guess < secret_number:
                print("Too low. Try again.")
                print(secret_number)
            else:
                print("Too high. Try again.")
                print(secret_number)
            # Check if the player has reached the maximum attempts
            if attempts == max_attempts:
                print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
guess_number()
