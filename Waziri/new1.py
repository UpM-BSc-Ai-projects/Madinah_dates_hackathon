import requests
import os
from bs4 import BeautifulSoup


def download_images_from_search(query, num_images, save_directory):
    search_url = f"https://www.bing.com/search?hl=en&tbm=isch&q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')

    os.makedirs(save_directory, exist_ok=True)

    count = 0
    for img in img_tags:
        if count >= num_images:
            break
        try:
            img_url = img.get('src')
            if img_url:
                img_response = requests.get(img_url)
                file_extension = img_url.split('.')[-1].split('?')[0]
                file_name = f"{query}_{count + 1}.{file_extension}"
                file_path = os.path.join(save_directory, file_name)

                with open(file_path, 'wb') as file:
                    file.write(img_response.content)

                print(f"Downloaded {file_name}")
                count += 1
        except Exception as e:
            print(f"An error occurred: {str(e)}")




# Example Usage
download_images_from_search("Date Tree", 20, "./dataset/date_tree")
download_images_from_search("Red Palm Weevil", 20, "./dataset/red_palm_weevil")