import json

def add_award_entry(file_name):
    # Initialize the new entry dictionary
    new_entry = {
        "genre": "award",
        "year": "2024"  # Default year
    }

    # Take user inputs for the required fields
    new_entry["award_name"] = input("Enter the award name: ").strip()
    new_entry["country"] = input("Enter the award country(default- India): ").strip() or "India"
    new_entry["who_awarded"] = input("Who was awarded? ").strip()
    new_entry["awardee_designation"] = input("Enter the designation of the awardee: ").strip()
    new_entry["description"] = input("Enter the description: ").strip()
    new_entry["month"] = input("Enter the month: ").strip()

    # Load existing data from the file
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty structure
        data = {"award_section": []}

    # Append the new entry to the award_section
    data["award_section"].append(new_entry)

    # Write the updated data back to the file
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    
    print("New award entry added successfully!")

# Run the function
file_name = "CA_awards.txt"
add_award_entry(file_name)