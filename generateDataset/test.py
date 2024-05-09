import requests
import os

# Google Custom Search API credentials
API_KEY = "AIzaSyA9ZWCZRyDTFf19UsDIG-9GBZhfPSzhBmo"
SEARCH_ENGINE_ID = "1781e97705db04d8d"

def download_images(query, num_images=10, download_path="images"):
    # Create the download directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Google Custom Search API endpoint
    search_url = "https://www.googleapis.com/customsearch/v1"
    
    # Parameters for the API request
    params = {
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query,
        "searchType": "image",
        "num": num_images
    }

    try:
        # Sending request to Google Custom Search API
        response = requests.get(search_url, params=params)
        data = response.json()

        # Downloading images
        for i, item in enumerate(data["items"]):
            image_url = item["link"]
            image_filename = os.path.join(download_path, f"{query}_{i+1}.jpg")
            print(f"Downloading image {i+1}/{num_images}: {image_url}")
            with open(image_filename, "wb") as f:
                f.write(requests.get(image_url).content)
    except Exception as e:
        print("An error occurred:", e)

# Example usage
if __name__ == "__main__":
    vip_name = input("Enter the VIP's name: ")
    download_images(vip_name)