import os
import pandas as pd

# Define the CSV file name
csv_file = 'date.csv'

# Define the headers for the CSV file
columns = ['Date ID', 'Date Type', 'Quality', 'Colour', 'Size', 'Price (per kg)']

# CHANGE THESE VALUES AS NEEDED, Then manually check each row for accuracy
default_date_type = 'Safawi'
default_quality = 'Medium'
default_colour = 'Golden'
default_size = 'Medium'
default_price_per_kg = '9SR - 15SR'


# CHANGE THIS FUNCTION AS NEEDED, This is just a simple example
def generate_date_id(counter):
    return f"WD10{counter:02d}"


def add_images_to_csv():
    # Load existing CSV if it exists, else create an empty DataFrame
    if os.path.exists(csv_file):
        existing_df = pd.read_csv(csv_file)
    else:
        existing_df = pd.DataFrame(columns=columns)

    # Get the current number of rows (to start the counter properly)
    start_counter = 1

    # Prepare a list to hold the new rows
    new_rows = []

    # Counter from 01 to 40
    for counter in range(start_counter, start_counter + 40):
        # Generate the Date ID
        date_id = generate_date_id(counter)

        # Append the new row with default values
        new_rows.append(
            [date_id, default_date_type, default_quality, default_colour, default_size, default_price_per_kg])
        print(f"Generated Date ID {date_id}.")

    # Convert the new rows to a DataFrame
    new_df = pd.DataFrame(new_rows, columns=columns)

    # Append new rows to the existing CSV
    new_df.to_csv(csv_file, index=False, mode='a', header=not os.path.exists(csv_file))
    print(f"Added {len(new_rows)} new rows to {csv_file}.")

add_images_to_csv()