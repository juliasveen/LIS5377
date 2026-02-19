import functions as f


def main():
    """program entry"""
    f.get_requirements()
    f.get_data()
    # Removed the missing select/slice functions to fix AttributeError
    f.get_stats()


if __name__ == "__main__":
    main()