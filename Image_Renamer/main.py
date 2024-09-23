import os
from PIL import Image

# Define the path to your dataset directory
dataset_dir = 'path_to_your_dataset'  # Modify this to your dataset directory path
categories = ['ambar']  # List of your date types (folders)

# Define the target size for resizing (224x224)
target_size = (224, 224)

# Function to resize and save images
def resize_image(image_path, target_size, save_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Resize the image
            img_resized = img.resize(target_size)
            # Save the resized image
            img_resized.save(save_path)
            print(f"Image resized and saved: {save_path}")
    except Exception as e:
        print(f"Error resizing {image_path}: {e}")

# Function to rename and process images
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
            image_path = os.path.join(category_path, image_name)

            # Skip non-image files
            if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                print(f"Skipping non-image file: {image_name}")
                continue

            # Create new image name
            new_image_name = f"{category}_{idx + 1}.jpg"
            new_image_path = os.path.join(category_path, new_image_name)

            # Resize and save the image
            resize_image(image_path, target_size, new_image_path)

            # Optionally, delete the old image
            if new_image_path != image_path:
                os.remove(image_path)
                print(f"Deleted original image: {image_path}")

# Run the function
rename_images()
