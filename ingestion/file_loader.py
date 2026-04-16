import pandas as pd
from decorator.log_decorator import log_execution

@log_execution # this is a decorator used to ensure proper logging of the function start and end 
def load_file(path):
    """
    Loads data from a CSV file
    """
    
    data = pd.read_csv(path)
    print("Loaded:", data.shape)  # shape function return rows and columns in the dataframe 
    return data