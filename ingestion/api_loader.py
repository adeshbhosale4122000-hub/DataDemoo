import pandas as pd

def load_from_api():
    """
    Simulates loading data from an API
    """
    print("Simulating API data...")

    data = [
        {"name": "api_user", "age": 30, "city": "Mumbai", "salary": 70000}
    ]

    return pd.DataFrame(data)