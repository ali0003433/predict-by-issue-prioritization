import numpy as np
import pandas as pd
import re


def fill_nulls(df):
    '''
    Fill null values with a zero value. 
    
    Args:
        df(Dataframe): Takes in a dataframe. 
    
    Returns:
        df(Dataframe): Dataframe with null values as zeros. 
    '''
    df = df.fillna(8)
    return df


def filter_col_with_regex(df, pattern):
    '''
    Search column names for regex pattern and return list.  
    
    Args: 
        df(Dataframe): The dataframe with the columns to be filtered. 
        pattern(str): Regex pattern to filter strings by. 
        
    Returns:
        col_list(list): List of columns that matches regex pattern. 
    '''
    col_list = []
    pattern = pattern
    for col in df.columns:
        if re.search(pattern, col):
            col_list.append(col)
    return col_list


def get_dummies(df_subset):
    '''
    Converts categorical integer values to string datatype and performs one hot encoding. 
    Args:
        df_subset(Dataframe): Takes in a slice or subset of the dataframe. 
    Returns:
        Same subset of dataframe but with dummy variables. 
    '''
    df_subset = df_subset.astype(str)
    df_dummies = pd.get_dummies(df_subset, drop_first=True)
    return df_dummies