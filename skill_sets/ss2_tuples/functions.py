def print_header():
    """Print the program header and requirements."""
    print("Python Tuples\n")
    print("Program Requirements:")
    print("Developer: Julia Sveen, BSIT")
    print("1. Tuples (Python data structure): *immutable* (cannot be changed!), ordered sequence of elements.")
    print("2. Tuples are immutable/unchangeable--that is, cannot insert, update, delete.")
    print("3. Create tuple using parentheses (typle): tuple = (include below list elements ).")
    print("4. Reassign tuple with, and w/o parentheses(), aka tuple \"packing\".")
    print("5. Use tuple (unpacking), that is, assign values from tuple to sequence of variables: elem1, elem2, elem3, elem4 = my_tuple.")
    print("6. Backward-engineer the following program.\n")


def demonstrate_tuple():
    """Demonstrate tuple operations."""
    # 3. Create tuple using parentheses
    my_tuple = (1, 'test', 3.14, True)

    print(f"Print my_tuple: {my_tuple}")

    # 5. Use tuple (unpacking)
    elem1, elem2, elem3, elem4 = my_tuple
    print("\nPrint my_tuple unpacking:")
    print(f"elem1={elem1}, elem2={elem2}, elem3={elem3}, elem4={elem4}")

    # Display number of my_tuple elements
    print(f"\nDisplay number of my_tuple elements: \n{len(my_tuple)}")

    # Print third element (Index 2)
    print(f"\nPrint third element in my_tuple: \n{my_tuple[2]}\n")

    # Print "slice" of my_tuple (second and third elements)
    # Note: Slice is [start:stop], where stop is exclusive.
    print(f"Print \"slice\" of my_tuple (second and third elements): \n{my_tuple[1:3]}\n")

    # 4. Reassign my_tuple using parentheses
    my_tuple = (1, 2, 3, 4)
    print("Reassign my_tuple using parentheses.")
    print(f"Print reassigned my_tuple: \n{my_tuple}\n")

    # 4. Reassign my_tuple using "packing" method (no parentheses)
    my_tuple = 5, 6, 7, 8
    print("Reassign my_tuple using \"packing\" method (no parentheses).")
    print(f"Print reassigned my_tuple: \n{my_tuple}\n")

    print("Delete my_tuple")
    del my_tuple
    print("Note: will generate error, if trying to print after delete, as it no longer exists.")
