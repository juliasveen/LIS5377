import random

def get_requirements():
    """Displays program requirements and developer information."""
    print("Developer: Julia Sveen") #
    print("Guessing Game!") #
    print("\nProgram Requirements:") #
    print("1. Create guessing game based upon pseudo-random numbers.") #
    print("2. Must perform data and range validation.") #
    print("\n***Resource(s):***") #
    print("Generate pseudo-random numbers: https://docs.python.org/3/library/random.html") #
    print("\nInput:") #

def get_valid_int(prompt, min_val=-1000, max_val=1000, label="Number"):
    """Generic function to handle int validation and range checking."""
    while True:
        try:
            val = int(input(prompt)) #
            if min_val <= val <= max_val: #
                return val
            else:
                print(f"{label} must be between {min_val} and {max_val}.\n") #
        except ValueError:
            print("Not an int! Try again.\n") #

def play_game(lower, upper):
    """Executes the guessing logic and tracks the number of attempts."""
    # Generate the secret number within the user's defined range
    secret_number = random.randint(lower, upper)
    tries = 0
    
    while True:
        # Range for guess isn't strictly defined in requirements, using same bounds
        guess = get_valid_int("Enter guess: ", label="Guess")
        tries += 1
        
        if guess < secret_number:
            print("Too low!\n") #
        elif guess > secret_number:
            print("Too high!") #
        else:
            print(f"Bingo! Number of tries: {tries}") #
            break