import os

input_folder = "data/input"
latest_file = sorted(os.listdir(input_folder))[-1]

INPUT_FILE = os.path.join(input_folder, latest_file)
OUTPUT_FILE = os.getenv("OUTPUT_FILE")  
LOG_LEVEL = os.getenv("LOG_LEVEL")