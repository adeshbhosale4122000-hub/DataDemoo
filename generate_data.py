import pandas as pd
import random
import os

# ensure folder exists
os.makedirs("data/input", exist_ok=True)

names = ["Daniyal", "Ali", "Sara", "John", "Aisha", "Rahul", "Priya", "Karan"]
cities = ["Mumbai", "Delhi", "Bangalore", "Pune", "Chennai", "Hyderabad"]

data = []

for i in range(10000):
    row = {
        "name": random.choice(names),
        "age": random.choice([20, 21, 22, 23, 24, 25, None]),
        "city": random.choice(cities + [None]),
        "salary": random.choice([40000, 50000, 60000, 70000, None])
    }
    data.append(row)

df = pd.DataFrame(data)

# generate file name automatically
file_count = len(os.listdir("data/input")) + 1
file_name = f"data/input/input_{file_count}.csv"

df.to_csv(file_name, index=False)

print(f"CSV created: {file_name}")