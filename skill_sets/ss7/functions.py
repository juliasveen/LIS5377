import random

def get_requirements():
    """Displays program requirements and resources."""
    print("Developer: Julia Sveen") #
    print("Pseudo-Random Number Lists!") #
    print("\nProgram Requirements:") #
    print("1. Create pseudo-random list of numbers.") #
    print("2. Sort pseudo-random list of numbers.") #
    print("3. Must perform data and range validation.") #
    
    print("\n***Resource(s):***") #
    print("Generate pseudo-random numbers: https://docs.python.org/3/library/random.html") #
    print("for loop with range() function: https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/") #
    print("\nInput:") #

def get_list_size():
    """Prompts for list size with data and range validation."""
    while True:
        try:
            size = int(input("Enter list size: ")) #
            if 1 <= size <= 10: #
                return size
            else:
                print("List size must be between 1 and 10.\n") #
        except ValueError:
            print("Not an int! Try again.\n") #

def create_list(size):
    """Generates a list of unique pseudo-random numbers using range."""
    # Based on the output, it generates a list containing numbers 1 through 'size' in random order
    my_list = list(range(1, size + 1)) #
    random.shuffle(my_list) #
    return my_list

def process_list(numbers):
    """Sorts and displays the list in original, ascending, and descending order."""
    print(f"\nOriginal pseudo-random number list: {numbers}") #
    
    # Sort ascending
    numbers.sort() #
    print(f"Sorted list (ascending): {numbers}") #
    
    # Sort descending
    numbers.sort(reverse=True) #
    print(f"Sorted list (descending): {numbers}") #