from decorator.log_decorator import log_execution

@log_execution  # decorator to ensure the logging of start and end of cleaning data 
def clean_data(data):
    cleaned_data = data.dropna().copy()  #copy to ensure dataset does not change 
    return cleaned_data