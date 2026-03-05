import functions as f

def main():
    """Main entry point for the pseudo-random list program."""
    # 1. Display requirements
    f.get_requirements()
    
    # 2. Get validated list size
    size = f.get_list_size()
    
    # 3. Create the random list
    random_numbers = f.create_list(size)
    
    # 4. Sort and display the results
    f.process_list(random_numbers)

if __name__ == "__main__":
    main()