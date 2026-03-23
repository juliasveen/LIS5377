def get_requirements():
    """Displays program requirements and developer information."""
    print("Developer: Julia Sveen")
    print("Simple Shopping Cart!")
    print("\nProgram Requirements:")
    print("1. Capture user-entered shopping items.")
    print("2. Retrieve cost for each item.")
    print("3. Print items, cost, and total of all items.")
    print("4. Must perform data and range validation.")
    print("\n***Extra credit (10 pts):***")
    print("    a. Request tax rate: between 1% and 10%.")
    print("    b. Print pre-tax total, total tax, and total amount with tax.")
    print("    c. Must perform data and range validation.")
    print("\n***Resource(s):***")
    print("Prompt user until valid response: https://www.python-engineer.com/posts/ask-user-for-input/")
    print("Print tabular data:")
    print("        https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data")
    print("        https://www.educba.com/python-print-table/")
    print("\nInput:")
    print("Enter -1 to stop program.\n")


def get_items():
    """Prompts user to enter item names until -1 is entered. Returns list of item names."""
    items = []
    item_num = 1

    while True:
        name = input(f"Enter item{item_num} name: ").strip()
        if name == "":
            print("No item name entered! Try again.\n")
            continue
        if name == "-1":
            print("Stopping list!\n")
            break
        items.append(name)
        item_num += 1

    return items


def get_cost(item_name):
    """Prompts user for a valid cost for the given item. Cost must be between $1 and $100."""
    while True:
        try:
            cost = float(input(f"Enter {item_name} cost: $"))
            if 1 <= cost <= 100:
                return cost
            else:
                print("Item cost must be between $1 and $100.\n")
        except ValueError:
            print("Not a float! Try again.\n")


def get_costs(items):
    """Retrieves costs for each item in the list. Returns list of costs."""
    costs = []
    for item in items:
        cost = get_cost(item)
        costs.append(cost)
    return costs


def print_table(items, costs):
    """Prints items and costs in tabular format, followed by the total."""
    print(f"{'Item':<10}{'Cost'}")
    for item, cost in zip(items, costs):
        print(f"{item:<10}{cost:.2f}")

    total = sum(costs)
    print(f"\nTotal: ${total:.2f}")
    return total


def get_tax_rate():
    """Prompts user for a valid tax rate between 1% and 10%. Returns the rate as a float."""
    while True:
        try:
            rate = float(input("\nEnter tax rate (1-10): "))
            if 1 <= rate <= 10:
                return rate
            else:
                print("Tax rate must be between 1% and 10%.")
        except ValueError:
            print("Not a float! Try again.")


def print_tax_summary(total, tax_rate):
    """Prints pre-tax total, total tax, and total with tax."""
    tax_amount = total * (tax_rate / 100)
    total_with_tax = total + tax_amount
    print(f"\nPre-tax total: ${total:.2f}")
    print(f"Total tax: ${tax_amount:.2f}")
    print(f"Total with tax: ${total_with_tax:.2f}")