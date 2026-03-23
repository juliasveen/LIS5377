import functions as f

def main():
    """Main entry point to coordinate the contact list flow."""
    f.get_requirements()

    # Collect email addresses from user
    emails = f.get_emails()

    if not emails:
        print("No emails entered. Exiting.")
        return

    # Build contacts dictionary: {email: phone}
    contacts = f.build_contacts(emails)

    # Print dictionary, keys, values, and items
    f.print_contacts(contacts)

    # Extra credit (a): Add first and last names
    contacts = f.add_names(contacts)
    print("\nContacts with names:")
    print(contacts)

    # Extra credit (b): Update and delete contacts
    contacts = f.update_contact(contacts)
    contacts = f.delete_contact(contacts)

    print("\nFinal contacts:")
    print(contacts)


if __name__ == "__main__":
    main()