import functions as f

def main():
    """Main entry point to coordinate the guessing game flow."""
    f.get_requirements()
    
    # Get range boundaries with validation
    while True:
        lower = f.get_valid_int("Enter lower number: ", label="Lower") #
        upper = f.get_valid_int("Enter upper number: ", label="Upper") #
        
        if lower <= upper: #
            break
        else:
            print("Lower number must be less than or equal to upper number! Try again!\n") #

    # Start the actual guessing loop
    f.play_game(lower, upper)

if __name__ == "__main__":
    main()