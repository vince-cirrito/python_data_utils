"""Set of functionalities to get an overview of a DataFrame
"""
import pandas as pd
import numpy as np
# example dataframe to put in unit test
df = pd.DataFrame({
    'numeric' : [1,2,3,4],
    'textual' : ['a', 'b', 'c', 'd'],
    'strange' : [(1,2), (2,2), (3,3), (4,4)]
 })

def df_screen(df):
    """first screening of dataframe
    TODO:
    - [] df size
    - [] column names
    - [] data type per column
    - [] min and max for number type
    - [] random datapoint for non_number
    """
    if isinstance(df, pd.core.frame.DataFrame):
        column_names = df.columns
        column_types = list(
            map(lambda x: type(x), df, 
                ['numeric', 'textual'])
            )