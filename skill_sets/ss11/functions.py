def get_requirements():
    """Displays program requirements and developer information."""
    print("Developer: Julia Sveen")
    print("Working with lists, dictionaries, and user-entered values.")
    print("\nProgram Requirements:")
    print("1. Write a program that prints all elements of a user-entered contact list.")
    print("2. Must perform data validation.")
    print("3. Dictionary key *must* be user's e-mail address.")
    print("4. ***Extra credit (20pts. Both are optional.):***")
    print("        a) Provide additional functionality to add contacts' first and last names (10 pts).")
    print("        b) Provide additional functionality to update *and* delete contacts (10 pts. Both required.).")
    print("\n***Resource(s):***")
    print("Dictionaries:")
    print("https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-dictionaries/cheatsheet")
    print("https://www.pythoncheatsheet.org/cheatsheet/dictionaries")
    print("\nInput:")
    print("Enter -1 to stop adding e-mails.\n")


def get_emails():
    """Prompts user to enter email addresses until -1 is entered. Returns list of emails."""
    emails = []
    count = 1

    while True:
        email = input(f"Enter email {count}: ").strip()
        if email == "-1":
            print("Stopping list!")
            break
        if email == "":
            print("No email entered! Try again.\n")
            continue
        emails.append(email)
        count += 1

    return emails


def get_phone(email):
    """Prompts user for a phone number for the given email. Returns phone string."""
    while True:
        phone = input(f"\n{email}, phone: \n").strip()
        if phone == "":
            print("No phone number entered! Try again.\n")
            continue
        return phone


def build_contacts(emails):
    """Builds and returns a contacts dictionary with email as key and phone as value."""
    contacts = {}
    for email in emails:
        phone = get_phone(email)
        contacts[email] = phone
    return contacts


def print_contacts(contacts):
    """Prints the full dictionary and its keys, values, and items."""
    print("\nPrinting dictionary:")
    print(contacts)

    print("\nPrinting dictionary keys:")
    print(contacts.keys())

    print("\nPrinting dictionary values:")
    print(contacts.values())

    print("\nPrinting dictionary items:")
    print(contacts.items())


def add_names(contacts):
    """Extra credit (a): Adds first and last names to each contact."""
    updated = {}
    for email, phone in contacts.items():
        first = input(f"\nEnter first name for {email}: ").strip()
        last = input(f"Enter last name for {email}: ").strip()
        updated[email] = {"phone": phone, "first": first, "last": last}
    return updated


def update_contact(contacts):
    """Extra credit (b): Updates the phone number for an existing contact."""
    email = input("\nEnter email to update: ").strip()
    if email in contacts:
        new_phone = input(f"\nEnter new phone for {email}: ").strip()
        if isinstance(contacts[email], dict):
            contacts[email]["phone"] = new_phone
        else:
            contacts[email] = new_phone
        print(f"{email} updated.")
    else:
        print("Email not found.\n")
    return contacts


def delete_contact(contacts):
    """Extra credit (b): Deletes a contact from the dictionary."""
    email = input("\nEnter email to delete: ").strip()
    if email in contacts:
        del contacts[email]
        print(f"{email} deleted.")
    else:
        print("Email not found.\n")
    return contacts