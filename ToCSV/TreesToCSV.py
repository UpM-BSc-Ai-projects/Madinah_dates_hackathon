import os
import pandas as pd

# Define the CSV file name for trees
csv_file = 'trees.csv'

# Define a dictionary to map the first letter of the image name to the tree type
tree_type_map = {
    'K': 'Sukkari',
    'Q': 'Saqi',
    'J': 'Ajwa',
    'A': 'Amber',
    'H': 'Helwa',
    'B': 'Barhi',
    'W': 'Safawi'
}

# Define the headers for the CSV file
columns = ['Image Name', 'Tree ID', 'Tree Type', 'Status', 'Age', 'Gender', 'Region']


# Function to extract the Tree ID by removing the suffix (_1, _2, etc.)
def extract_tree_id(image_name):
    return image_name.rsplit('_', 1)[0] if '_' in image_name else image_name


# Function to process and add tree images to the CSV
def add_tree_images_to_csv(directory):
    # Prepare a list to hold the data rows
    rows = []

    # Go through all files in the directory
    for image_name in os.listdir(directory):
        if image_name.endswith('.jpg'):  # Only process .jpg images
            # Extract the Tree ID and first letter for tree type
            tree_id = extract_tree_id(image_name)
            first_letter = image_name[0].upper()
            tree_type = tree_type_map.get(first_letter, 'Unknown')

            # Set default values for status, age, gender, and region
            status = 'Healthy'
            age = '25'  # Placeholder, modify as needed
            gender = 'Male'  # Placeholder, modify as needed
            region = "Abyar 'Ali"  # Placeholder, modify as needed

            # Append the row to the list
            rows.append([image_name, tree_id, tree_type, status, age, gender, region])

    # Convert the list to a DataFrame
    df = pd.DataFrame(rows, columns=columns)

    # Check if the CSV file already exists
    write_header = not os.path.exists(csv_file)  # Only write headers if the file doesn't exist
    df.to_csv(csv_file, index=False, mode='a', header=write_header)
    print(f"Added new rows to {csv_file}. Headers written: {write_header}")

# Example usage:
# add_tree_images_to_csv(r"C:\Users\themi\OneDrive\Pictures\Hackathon\Trees\Be2r Ali Farm\AT3001")


