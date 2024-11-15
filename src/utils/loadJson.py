import json

def loadJson(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file at {file_path} could not be decoded. Please ensure it is valid JSON.")
    return None
