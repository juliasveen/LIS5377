def get_requirements():
    print("This program demonstrates the use of dictionaries in Python.")
    print("It includes functions to create, parse, count, add, update, and delete elements in a dictionary.")

def get_dictionary():
    state_capitals={
        "Alaska":"Juneau",
        "Texas":"Austin",
        "California":"Sacramento",
        "Montana":"Helena",
        "New Mexico":"Santa Fe"
    }

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
    print("\nCount")

def count_dictionary(your_dictionary):

def add_element(your_dictionary):

def update_element(your_dictionary):

def delete_element(your_dictionary):

def delete_dictionary(your_dictionary):
