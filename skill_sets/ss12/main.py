import functions as f


def main():
    """Main entry point to coordinate the file system navigation program."""
    f.get_requirements()

    while True:
        f.print_cwd()
        f.print_menu()

        cmd = f.get_command()

        if cmd == 1:
            f.list_files()
        elif cmd == 2:
            f.go_up()
        elif cmd == 3:
            f.go_down()
        elif cmd == 4:
            f.count_files()
        elif cmd == 5:
            f.get_size()
        elif cmd == 6:
            f.search_files()
        elif cmd == 7:
            print("\nStopping program!")
            break


if __name__ == "__main__":
    main()