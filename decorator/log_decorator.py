from utils.logger import get_logger

logger = get_logger(__name__) #creates logger for this file 

def log_execution(func): # calling function inside another function 
    """
    Decorator to log start and end of a function
    """
    def wrapper(*args, **kwargs): # wrapper is used if we want to run something before our function 
        logger.info(f"Starting {func.__name__}")
        
        result = func(*args, **kwargs)
        
        logger.info(f"Finished {func.__name__}")
        
        return result
    return wrapper