from decorator.log_decorator import log_execution

@log_execution # logger that ensures when saving of file starts and end 
def save_file(data, path):
    data.to_csv(path, index=False)