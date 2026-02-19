import pandas as pd
df = pd.read_csv('us_data.csv')

def get_requirements():
    print("\nPandas DataFrames and Series Data Structures")
    print("\nProgram Requirements:\n"
        "Developer: Julia Sveen, BSIT\n"
        "1. Working with pandas dataframes and series data structures, for tabular data handling.\n"
        "2. Dataframe: two-dimensional labeled data structure (rows/cols).\n"
        "3. Dataframe: series collection. Each column is series sharing same index.\n"
        "4. Isolation rows and columns.\n"
        "5. Series: one-dimensional labeled array.\n"
        "6. Working with boolean data.\n")
    
def get_data():
    print("Print pandas version:")
    print(pd.__version__)

    print("\nDisplay data:")
    print(df)
    print("\nDisplay type:")
    print(type(df))

def get_bool_data():
    print("\nPrint boolean data:")
    df_bool=(df =='DE')
    print(df_bool)

    print("\nDisplay type:")
    print(type(df_bool))
    return df_bool

def count_bool_cols(my_bool):
    bool_sum_cols=my_bool.sum()
    print("\nPrint boolean cols:")
    print(bool_sum_cols)

    print("\nDisplay type:")
    print(type(bool_sum_cols))

def count_bool_rows(my_bool):
    bool_sum_rows=my_bool.sum(axis=1)
    print("\nPrint boolean rows:")
    print(bool_sum_rows)

    print("\nDisplay type:")
    print(type(bool_sum_rows))

def count_bool_total(my_bool):
    bool_sum_total=my_bool.sum().sum()
    print("\nPrint boolean total:")
    print(bool_sum_total)

    print("\nDisplay type:")
    print(type(bool_sum_total))

def get_series_data():
    print("\nPrint square miles as series:")
    my_series=df['total square miles']
    print(my_series)

    print("\nDisplay type:")
    print(type(my_series))
    return my_series

def evaluate_series_data(s_data):
    num_states = (s_data > 100000).sum()
    print("\nPrint number of states with 100,000 or more square miles:") 
    print(num_states)

    print("\nDisplay type:")
    print(type(num_states))

def convert_dataframe_to_numpy_array(my_bool):
    print("\nDataframe converted to numpy array (ndarray) using \"values\" attribute: ")

    print("\nDisplay original my_bool type:")
    print(type(my_bool))

    print("\nDisplay converted my_bool type using \"values\" attribute:")
    print(type(my_bool.values))

    print("\nDisplay NumPy array using \"values\" attribute:")
    print(my_bool.values)

    print("\nPrint total number of states with two-letter abbreviation == to \"DE\":")
    print(my_bool.values.sum())
          

