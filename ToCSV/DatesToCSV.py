import os
import pandas as pd

# Define the CSV file name
csv_file = 'date.csv'

# Define a dictionary to map the first letter of the image name to the date type
date_type_map = {
    'K': 'Sukkari',
    'Q': 'Saqi',
    'J': 'Ajwa',
    'A': 'Amber',
    'H': 'Helwa',
    'B': 'Barhi',
    'W': 'Safawi'
}

# Define the headers for the CSV file
columns = ['Image Name', 'Date ID', 'Date Type', 'Quality', 'Colour', 'Size', 'Price (in Kg)']


# Function to extract the Date ID by removing the suffix (_1, _2, etc.)
def extract_date_id(image_name):
    return image_name.rsplit('_', 1)[0] if '_' in image_name else image_name


# Function to process and add images to the CSV
def add_images_to_csv(directory):
    # Prepare a list to hold the data rows
    rows = []

    # Go through all files in the directory
    for image_name in os.listdir(directory):
        if image_name.endswith('.jpg'):  # Only process .jpg images
            # Extract the Date ID and first letter for date type
            date_id = extract_date_id(image_name)
            first_letter = image_name[0].upper()
            date_type = date_type_map.get(first_letter, 'Unknown')

            # Set default values for quality, colour, size, and price
            quality = 'High'
            colour = 'Golden Brown'
            size = 'Medium'
            price_per_kg = '15SR - 50SR'

            # Append the row to the list
            rows.append([image_name, date_id, date_type, quality, colour, size, price_per_kg])

    # Convert the list to a DataFrame
    df = pd.DataFrame(rows, columns=columns)

    # Check if the CSV file already exists
    write_header = not os.path.exists(csv_file)  # Only write headers if the file doesn't exist
    df.to_csv(csv_file, index=False, mode='a', header=write_header)
    print(f"Added new rows to {csv_file}. Headers written: {write_header}")

# Example usage:
add_images_to_csv(r"C:\Users\themi\OneDrive\Pictures\Hackathon\Dates")


