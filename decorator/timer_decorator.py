import time

def timer(func):
    """
    Decorator to measure execution time of a function
    """
    
    def wrapper(*args, **kwargs):
        
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        
        print(f"{func.__name__} took {end - start:.4f} sec")
        
        return result
    return wrapper