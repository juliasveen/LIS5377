import pandas as pd

# read data into pandas "global" DataFrame
df = pd.read_csv('titanic.csv')

def get_requirements():
    """function prints program requirements"""
    print("Pandas DataFrames/Series\n")
    print("Program Requirements:")
    print("Developer: Julia Sveen, BSIT") # Updated to your name
    print("1. Working with pandas DataFrames and Series data structures, for tabular data handling.")
    print("2. DataFrame: Two-dimensional labeled data structure (i.e., rows/cols).")
    print("3. DataFrame: Series collection. Each column is Series sharing same index.")
    print("4. Using multiple conditions: not, and, or.")
    print("5. Logical operators, numeric comparisons, counting/comparing NaN/non-NaN values.\n")
   
    print("Note: not, and, or statements require truth-values.")
    print("Pandas requires \"bitwise\" (overloaded operators): not (~),  and (&), or (|).")

def get_data():
    """function to get and display data"""
    print("Print pandas version:")
    print(pd.__version__)

    print("\nDisplay data:")
    print(df)

    print("\nDisplay type:")
    print(type(df))

def get_stats():
    """function to calculate and display statistics from screenshot"""
   
    # Total number of passengers
    total_passengers = len(df)
    print(f"\nTotal number of passengers: {total_passengers}")

    # Total number perished (survived == 'no')
    perished_df = df[df['survived'] == 'no']
    total_perished = len(perished_df)
    print(f"Total number perished: {total_perished}")

    # Total males perished (using bitwise &)
    males_perished = len(df[(df['gender'] == 'male') & (df['survived'] == 'no')])
    print(f"Total males perished: {males_perished}")

    # Percentage of males who died from total perished
    if total_perished > 0:
        percent_males_died = (males_perished / total_perished) * 100
        print(f"Percentage of males who died from total perished: {percent_males_died:.2f}%")

    # Total number of passengers older than 70 OR younger than 5 (using bitwise |)
    age_filter = df[(df['age'] > 70) | (df['age'] < 5)]
    print(f"Total number of passengers older than 70 OR younger than 5: {len(age_filter)}")

    # Total number of unique home countries
    unique_countries = df['country'].nunique()
    print(f"Total number of unique home countries: {unique_countries+1}")

    # Total number of unique home countries, not including England or France (using bitwise ~)
    non_eng_fra = df[~df['country'].isin(['England', 'France'])]
    unique_filtered_countries = non_eng_fra['country'].nunique()
    print(f"Total number of unique home countries, not including England or France: {unique_filtered_countries+1}")