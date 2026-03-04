from datetime import datetime
import os

def generate_log(data):

    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # STEP 2: Generate filename
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    # STEP 3: Write log entries to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation
    print(f"Log file created: {filename}")

    return filename