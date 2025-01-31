import json
import os
import shutil

def add_scheme_entry(file_name):
    # Initialize the new entry dictionary
    new_entry = {
        "year": "2024"  # Default year
    }

    # Take user inputs for the required fields
    print("Please enter the details for the new scheme entry.")
    new_entry["scheme_name"] = input("Enter the scheme name: ").strip()
    new_entry["under_ministry"] = input("Enter the ministry (leave blank if none): ").strip()
    
    # Handle statements as a set-like structure
    statements = input("Enter the statements (comma-separated): ").split(",")
    new_entry["statements"] = set(statement.strip() for statement in statements)

    new_entry["whatItis"] = input("What it is (e.g., scheme, policy, etc.): ").strip()
    new_entry["description"] = input("Enter the description (leave blank for 'no description'): ").strip() or "no description"
    new_entry["month"] = input("Enter the month: ").strip()

    # Backup the file to prevent data loss
    if os.path.exists(file_name):
        shutil.copy(file_name, file_name + ".backup")

    # Check if the file exists and read the data
    data = {"schemes": []}
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON file detected. A backup has been saved as '{file_name}.backup'.")
            print("Please fix the JSON file manually or start fresh.")

            # Do not reset the file automatically to prevent accidental data loss
            return

    # Append the new entry to the schemes list
    data["schemes"].append(new_entry)

    # Convert the statements back to JSON-compatible lists for saving
    for scheme in data["schemes"]:
        scheme["statements"] = list(scheme["statements"])

    # Write the updated data back to the file
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    print("New scheme entry added successfully!")

# Specify the text file name
file_name = "CA_schemes.txt"

# Call the function to add a new scheme entry
add_scheme_entry(file_name)