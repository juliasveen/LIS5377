def get_requirements():
    print("Python Dictionaries")
    print("Program Requirements:")
    print("\nDeveloper: Julia Sveen, BSIT")
    print("1. Dictionaries (Python data structure): unordered key:value pairs.")
    print("2. Dictionary: an associative array (also known as hashes).")
    print("3. Any key in a dictionary is associated (or mapped) to a value (i.e., any Python data type).")
    print("4. Keys: must be of immutable type (string, number or tuple with immutable elements) and must be unique.")
    print("5. Values: can be any data type and can repeat.")
    print("6. Dictionaries have key:value pairs instead of single values; differentiating a dictionary from a set.")
    print("7. Two methods to create dictionaries:")
    print("   a. Initialize dictionary with key/value pairs.")
    print("   b. Create empty dictionary, using curly braces {}: my_dictionary = {}")
    print("      Then, assign values to keys: my_dictionary['key1'] = 'some value'")
    print("8. Backward-engineer the following program.")


def get_dictionary():
    state_capitals={
        "Alaska":"Juneau",
        "Texas":"Austin",
        "California":"Sacramento",
        "Montana":"Helena",
        "New Mexico":"Santa Fe"
    }
    print("\nPrint dictionary: ")
    print(state_capitals)
    print("\nPrint data structure types:")
    print(type(state_capitals))
    return state_capitals
 

def parse_dictionary(my_dictionary):
    print("\nReturn dictionary's (key, value) pairs, built-in function:")
    print(my_dictionary.items())

    print("\nOr, use looping structure to return dictionary's (key, value) pairs, built-in function:")
    for k, v in my_dictionary.items():
        print("key:", k, "value:", v,sep="")

    print("\nDisplay all keys, built-in function:")
    print(my_dictionary.keys())

    print("\nDisplay all values in the dictionary, built-in function:")
    print(my_dictionary.values())

    print("\nPrint value using key:")
    print(my_dictionary['Alaska'])

def count_dictionary(my_dictionary):
    print("\nCount number of items (key:value pairs) in dictionary: ")
    print(len(my_dictionary))

def add_element(my_dictionary):
    my_dictionary["Arizona"] = "Scottsdale"

    print("\nPrint dictionary after added element: ")
    print(my_dictionary)

def update_element(my_dictionary):
    my_dictionary["Arizona"] = "Phoenix"

    print("\nPrint dictionary after updated element: ")
    print(my_dictionary)

def delete_element(my_dictionary):
    print("\nDelete \"Arizona\" element:")
    del my_dictionary["Arizona"]

    print("\nPrint dictionary after deleted element:")
    print(my_dictionary)

def delete_dictionary(my_dictionary):
    print("\nDelete all dictionary elements: ")
    my_dictionary.clear()
    print(my_dictionary)
    print(type(my_dictionary))

    del my_dictionary