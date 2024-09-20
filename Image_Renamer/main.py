import os
from PIL import Image

# Define the path to your dataset directory
dataset_dir = ''  # Modify this to your dataset directory path
categories = ['ambar']  # List of your date types (folders)

# Define the target size for resizing (224x224)
# target_size = (224, 224)


# Function to rename and resize images
def rename_images():
    for category in categories:
        category_path = os.path.join(dataset_dir, category)

        # Check if the folder exists
        if not os.path.exists(category_path):
            print(f"Directory {category_path} does not exist.")
            continue

        # Get all image files in the folder
        images = os.listdir(category_path)

        # Loop through each image and process it
        for idx, image_name in enumerate(images):
            try:
                image_path = os.path.join(category_path, image_name)

                # Open the image file
                with Image.open(image_path) as img:
                    # Resize the image
                    # img_resized = img.resize(target_size)

                    # Create new image name
                    new_image_name = f"{category}_{idx + 1}.jpg"
                    new_image_path = os.path.join(category_path, new_image_name)

                    # Save the resized image with the new name
                    img_resized.save(new_image_path)

                    # Optionally, delete the old image
                    if new_image_path != image_path:
                        os.remove(image_path)

                    print(f"Processed: {new_image_name}")

            except Exception as e:
                print(f"Error processing {image_name}: {e}")


# Run the function
rename_images()
