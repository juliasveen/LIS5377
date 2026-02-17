import functions as f

def main():
    f.get_requirements()
    my_dictionary=f.get_dictionary()
    f.parse_dictionary(my_dictionary)
    f.count_dictionary(my_dictionary)
    f.add_element(my_dictionary)
    f.update_element(my_dictionary)
    f.delete_element(my_dictionary)
    f.delete_dictionary(my_dictionary)

if __name__ == "__main__":    main()