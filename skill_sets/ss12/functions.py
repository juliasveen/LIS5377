import os


def get_requirements():
    """Displays program requirements and developer information."""
    print("Developer: Julia Sveen")
    print("Program provides file system navigation and information.")
    print("\nProgram Requirements:")
    print("1. Write program functions that navigate and display file system information.")
    print("2. Create and display program menu.")
    print("3. Must prevent incorrect command input.")
    print("\n***Resource(s):***")
    print("Python os package: https://docs.python.org/3/library/os.html")
    print("\nInput:")


def print_menu():
    """Prints the navigation menu."""
    print("\nMENU:")
    print("1 List")
    print("2 Up")
    print("3 Down")
    print("4 Count")
    print("5 Size")
    print("6 Search")
    print("7 Quit")


def print_cwd():
    """Prints the current working directory."""
    print(f"\nCurrent working directory:")
    print(os.getcwd())


def list_files():
    """Lists all files and directories in the current working directory."""
    cwd = os.getcwd()
    print(f'\nAll files and directories in "{cwd}":')
    for entry in os.listdir(cwd):
        print(entry)


def go_up():
    """Navigates one directory level up."""
    parent = os.path.dirname(os.getcwd())
    os.chdir(parent)


def go_down():
    """Prompts user for a directory name and navigates into it."""
    dir_name = input("Enter directory name: ").strip()
    target = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(target):
        os.chdir(target)
    else:
        print(f"Directory '{dir_name}' not found.")


def count_files():
    """Counts and prints the total number of files and directories in the current directory."""
    entries = os.listdir(os.getcwd())
    print(f"Total files: {len(entries)}")


def get_size():
    """Calculates and prints the total size of all files in the current directory."""
    total_bytes = 0
    for entry in os.listdir(os.getcwd()):
        full_path = os.path.join(os.getcwd(), entry)
        if os.path.isfile(full_path):
            total_bytes += os.path.getsize(full_path)

    total_kb = total_bytes / 1024
    total_mb = total_kb / 1024
    total_gb = total_mb / 1024

    print(f"\nTotal size:")
    print(f"{total_bytes:,} bytes")
    print(f"{total_kb:.2f} KB")
    print(f"{total_mb:.2f} MB")
    print(f"{total_gb:.4f} GB")


def search_files():
    """Prompts user for a search pattern and prints all matching file paths recursively."""
    pattern = input("Enter file name: ").strip()
    cwd = os.getcwd()
    print(f"\nFile paths for {pattern}:")
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if pattern in file:
                print(os.path.join(root, file))


def get_command():
    """Prompts user for a valid menu command (1-7). Returns the integer command."""
    while True:
        try:
            cmd = int(input("\nEnter command: "))
            if 1 <= cmd <= 7:
                return cmd
            else:
                print("Command must be between 1 and 7.")
        except ValueError:
            print("Not an int! Try again.")