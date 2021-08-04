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
    - [] sample per column
    - [] count of NAs per column
    - [] count of NUlls
    - [] count of zeros
    """
    if isinstance(df, pd.core.frame.DataFrame):
        #col names
        column_names = list(df.columns)

        #
