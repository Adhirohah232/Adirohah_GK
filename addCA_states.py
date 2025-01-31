import json

# Function to add an entry to the file
def add_entry_to_current_affairs(file_name):
    # Initialize a dictionary for the new entry
    new_entry = {}
    
    # Take inputs from the user
    new_entry["genre"] = "state"  # Genre is fixed as 'state'
    new_entry["state"] = input("Enter the state: ").strip()
    new_entry["city"] = input("Enter the city (leave blank if not applicable): ").strip()
    new_entry["term_to_ask"] = input("Enter the term to ask: ").strip()
    new_entry["scheme"] = int(input("Is it a scheme? Enter 1 for Yes, 0 for No: ").strip())
    new_entry["whatItis"] = input("What it is (e.g., launched, inaugurated): ").strip()
    new_entry["description"] = input("Enter the description: ").strip()
    new_entry["month"] = input("Enter the month: ").strip()
    new_entry["year"] = input("Enter the year (default is 2024): ").strip() or "2024"

    # Load the existing data from the file
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty list
        data = {"ca": []}
    
    # Append the new entry
    data["ca"].append(new_entry)
    
    # Write the updated data back to the file
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    
    print("New entry added successfully!")

# Run the function
file_name = "current_affairs.txt"
add_entry_to_current_affairs(file_name)