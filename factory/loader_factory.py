from ingestion.file_loader import load_file
from ingestion.api_loader import load_from_api

def get_loader(source_type):
    """
    Returns the appropriate loader function based on source type
    """

    if source_type == "file":
        return load_file

    elif source_type == "api":
        return load_from_api

    else:
        raise ValueError("Invalid source type")