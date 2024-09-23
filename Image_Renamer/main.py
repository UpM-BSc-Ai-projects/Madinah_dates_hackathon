import os
from PIL import Image

# Define the path to your dataset directory
dataset_dir = ''  # Modify this to your dataset directory path
categories = ['ambar']  # List of your date types (folders)

# Define the target size for resizing (224x224)
target_size = (224, 224)


# Function to rename and replace the original image
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

            # Rename the file (move the image to the new path with the new name)
            os.rename(image_path, new_image_path)
            print(f"Renamed {image_name} to {new_image_name}")


# Function to resize and save images
def resize_images():
    for category in categories:
        category_path = os.path.join(dataset_dir, category)

        # Check if the folder exists
        if not os.path.exists(category_path):
            print(f"Directory {category_path} does not exist.")
            continue

        # Get all image files in the folder
        images = os.listdir(category_path)

        # Loop through each image and process it
        for image_name in images:
            image_path = os.path.join(category_path, image_name)

            # Skip non-image files
            if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                print(f"Skipping non-image file: {image_name}")
                continue

            try:
                # Open the image file
                with Image.open(image_path) as img:
                    # Resize the image
                    img_resized = img.resize(target_size)

                    # Save the resized image (replace the original image)
                    img_resized.save(image_path)
                    print(f"Resized and replaced: {image_name}")

            except Exception as e:
                print(f"Error resizing {image_name}: {e}")


# Run the functions
rename_images()  # To rename images without resizing
#resize_images()  # To resize images separately if needed