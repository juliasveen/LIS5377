def print_header():
    """Print the program header and requirements."""
    print("Python Lists\n")
    print("Program Requirements:")
    print("Developer: Julia Sveen, BSIT")
    print("1. Lists (Python data structure): mutable, ordered sequence of elements.")
    print("2. Lists are mutable/changeable--that is, can insert, update, delete.")
    print("3. Create two lists - using square brackets [list items]: list = [include below list elements here...].")
    print("4. Backward-engineer the following program.\n")


def demonstrate_list1():
    """Demonstrate list operations on list1."""
    # Create list1
    list1 = [1, 'test', 3.14, True]
    print("Print list1:", list1)

    # Append '@' character to end of list1
    list1.append('@')
    print("\nAppend '@' character to end of list1:")
    print(list1)

    # Insert number 6 at beginning of list1
    list1.insert(0, 6)
    print("\nInsert number 6 at beginning of list1:")
    print(list1)

    # Display number of list1 elements
    print("\nDisplay number of list1 elements:")
    print(len(list1))

    # Reverse list1
    list1.reverse()
    print("\nReverse list1:")
    print(list1)

    # Remove last list1 element
    list1.pop()
    print("\nRemove last list1 element:")
    print(list1)

    # Delete second element from list1 by index (index 1)
    del list1[1]
    print("\nDelete second element from list1 by index (note: index 1 = 2nd element):")
    print(list1)

    # Delete element from list1 by value (3.14)
    list1.remove(3.14)
    print("\nDelete element from list1 by value (3.14):")
    print(list1)

    # Delete all elements from list1
    list1.clear()
    print("\nDelete all elements from list1:")
    print(list1)


def demonstrate_list2():
    """Demonstrate list operations on list2."""
    # Create list2
    list2 = ['test', 'a', 'new', 'list']
    print("\nPrint list2:", list2)

    # Sort list2 alphabetically
    list2.sort()
    print("\nSort elements in list2 alphabetically - using sort():")
    print(list2)

    # Sort list2 reverse alphabetically
    list2.sort(reverse=True)
    print("\nSort elements in list2 reverse alphabetically - using sort():")
    print(list2)
