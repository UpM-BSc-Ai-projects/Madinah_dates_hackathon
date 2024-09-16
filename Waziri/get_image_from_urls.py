import requests
import os
from bs4 import BeautifulSoup


def get_image_urls_from_webpage(url):
    try:
        # Send a GET request to the webpage URL
        response = requests.get(url)
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all image tags (usually <img>), you might need to adjust for specific sites
        img_tags = soup.find_all('img')

        # Extract image URLs
        image_urls = []
        for img in img_tags:
            img_url = img.get('src')  # Get the 'src' attribute of the <img> tag
            if img_url:
                # Ensure the URL is absolute (full URL), or modify if it's relative
                if not img_url.startswith(('http://', 'https://')):
                    img_url = requests.compat.urljoin(url, img_url)
                image_urls.append(img_url)

        return image_urls
    except Exception as e:
        print(f"An error occurred while fetching image URLs: {str(e)}")
        return []


def download_images(image_urls, save_directory):
    os.makedirs(save_directory, exist_ok=True)

    for i, image_url in enumerate(image_urls):
        try:
            # Send a GET request to the image URL
            response = requests.get(image_url)
            # Check if the request was successful
            if response.status_code == 200:
                # Extract the image extension
                file_extension = image_url.split('.')[-1]
                # Generate a file name
                file_name = f"image_{i + 1}.{file_extension}"

                # Create the full file path
                file_path = os.path.join(save_directory, file_name)

                # Open the file and write the image content
                with open(file_path, 'wb') as file:
                    file.write(response.content)

                print(f"Image {file_name} successfully downloaded.")
            else:
                print(f"Failed to download {image_url}. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred while downloading {image_url}: {str(e)}")


# Example Usage
webpage_url = "https://www.bing.com/images/search?q=rhynchophorus+ferrugineus+&FORM=HDRSC3"  # Replace with the actual URL
save_directory = "./downloaded_images"

# Step 1: Get all image URLs from the webpage
image_urls = get_image_urls_from_webpage(webpage_url)

# Step 2: Download the images
download_images(image_urls, save_directory)