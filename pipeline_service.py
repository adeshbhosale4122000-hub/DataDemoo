import os
from factory.loader_factory import get_loader
from processing.cleaner import clean_data
from processing.transformer import transform_data
from processing.validator import validate_data
from storage.file_writer import save_file

from config.config import INPUT_FILE, OUTPUT_FILE


class PipelineService:

    def __init__(self):
        #  this part does store the input and output file paths from config 
        self.input_path = INPUT_FILE      # stored them as class variables so can be reused
        self.output_path = OUTPUT_FILE

    def run(self):
        print("Pipeline started...")

        # Step 1:- Load data(from loader file)
        loader = get_loader("file")
        data = loader(self.input_path)

        #  Step 2:- Is to Validate data
        data = validate_data(data)

        #  Step 3: Clean data
        data = clean_data(data)

        # Step 4: Transform data
        data = transform_data(data)

        # get input file name
        file_name = os.path.basename(self.input_path)

        # replace input to output
        output_name = file_name.replace("input", "output")

        # create full output path
        output_path = os.path.join("data/output", output_name)

        # Step 5: Save data
        save_file(data, output_path)

        print("Pipeline finished successfully")