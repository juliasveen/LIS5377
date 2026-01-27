def print_header():
    """Print the program header and requirements."""
    print("Python Sets - like mathematical sets\n")
    print("Program Requirements:")
    print("Developer: Julia Sveen, BSIT")
    print("1. Sets (Python data structure): mutable, heterogeneous, unordered sequence of elements, CANNOT contain duplicate values.")
    print("2. Sets are mutable/changeable--that is, can insert, update, delete.")
    print("3. While sets are mutable/changeable, they cannot contain other mutable items like list, set or dictionary--that is, elements contained in set must be immutable.")
    print("4. Also, since sets are unordered, CANNOT use indexing (or, slicing) to access, update, or delete elements.")
    print("5. Two methods to create sets: ")
    print("   a. Using curly braces { set }: set1 = {include below set elements here...}.")
    print("   b. Using set() function: set1 = set(<iterable>).")
    print("6. Backward-engineer the following program.\n")


def demonstrate_set_creation():
    """Demonstrate different methods to create sets."""
    # 5. Two methods to create sets:
    # a. Curly brackets
    set1 = {2, "test", 3.14, True}
    print(f"Print set1 created using curly brackets: \n{set1}\n")
    print(f"Print set1 type: \n{type(set1)}\n")

    # b. set() function with list
    set2 = set([2, "test", 3.14, True])
    print(f"Print set2 created using set() function with list: \n{set2}\n")
    print(f"Print set2 type: \n{type(set2)}\n")

    # c. set() function with tuple
    set3 = set((2, "test", 3.14, True))
    print(f"Print set3 created using set() function with tuple: \n{set3}\n")
    print(f"Print set3 type: \n{type(set3)}\n")


def demonstrate_set_modifications():
    """Demonstrate set modification operations."""
    set1 = {2, "test", 3.14, True}
    
    print(f"Display number of set1 elements: \n{len(set1)}\n")

    # Add element
    set1.add(5)
    print(f"Add set element (5) using add() method: \n{set1}\n")
    print(f"Display number of set1 elements: \n{len(set1)}\n")

    # Update set (Note: True=1, so 1 is a duplicate. 2 also exists.)
    set1.update([1, 2, 3, 4])
    print(f"Display updated set1 elements (updated with 1, 2, 3, 4): \n{set1}\n")
    print(f"Display number of set1 elements: \n{len(set1)}\n")

    # Discard vs Remove
    set1.discard(4)  # Will not error if 4 is missing
    print(f"Discard 4: \n{set1}\n")
    print(f"Length of set1: \n{len(set1)}\n")

    set1.remove('test')  # Will raise KeyError if 'test' is missing
    print(f"Remove 'test': \n{set1}\n")
    print(f"Length of set1: \n{len(set1)}\n")

    # Math operations
    print(f"Display minimum value (Note: True=1): \n{min(set1)}\n")
    print(f"Display maximum value: \n{max(set1)}\n")
    print(f"Display sum of values: \n{sum(set1)}\n")

    # Delete all elements
    set1.clear()
    print(f"Delete all set elements: \n{set1}\n")
    print(f"Length of set1: \n{len(set1)}")
