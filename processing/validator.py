from constants.constants import REQUIRED_COLUMNS
from exceptions.custom_exception import ValidationError  # validation error is class 

def validate_data(data):
    """
    Validates if required columns exist in the dataset
    """

    print("Validating data...")

    # Check columns if present or not 
    for col in REQUIRED_COLUMNS:
        if col not in data.columns:
            raise ValidationError(f"Missing column: {col}")

    print("Validation passed ✅")

    return data