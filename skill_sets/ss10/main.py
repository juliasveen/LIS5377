import functions as f

def main():
    """Main entry point to coordinate the shopping cart flow."""
    f.get_requirements()

    # Collect item names from user
    items = f.get_items()

    if not items:
        print("No items entered. Exiting.")
        return

    # Collect costs for each item
    costs = f.get_costs(items)

    # Print table and get total
    total = f.print_table(items, costs)

    # Extra credit: tax calculation
    tax_rate = f.get_tax_rate()
    f.print_tax_summary(total, tax_rate)


if __name__ == "__main__":
    main()