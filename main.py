from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

@app.route("/")
def default_output():
    # load environment variables from .env file
    # load_dotenv()
    # access the API key from environment variables
    # Note: We need a custom API key seperate from GEMINI to make calls to the custom search engine API
    # gemini_api_key = os.getenv("GOOGLE_API_KEY")
    # search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    # custom_search_engine_api_key = os.getenv("CUSTOM_ENGINE_SEARCH_KEY")

    # loop through the different city locations
    city_image_urls = []

    # default set dictionary for the time being
    dictionary = ["New York", "Paris", "Istanbul"]

    for city_name in dictionary:
        city_image_urls.append(get_image_url(city_name, 1))

    # return the city urls as a response
    return jsonify(city_image_urls)

def get_google_images(query, api_key, cse_id, num_images=10):
    url = f"https://www.googleapis.com/customsearch/v1?"
    params = {
        "q": query,
        "searchType": "image",
        "key": api_key,
        "cx": cse_id,
        "num": num_images
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'items' in data:
        image_urls = [item['link'] for item in data['items']]
        return image_urls
    else:
        return None

# Query for image URL
def get_image_url(query, num_images):
    # load environment variables from .env file
    load_dotenv()

    # access the API key from environment variables
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    custom_search_engine_api_key = os.getenv("CUSTOM_ENGINE_SEARCH_KEY")

    # Get image URLs
    image_urls = get_google_images(query, custom_search_engine_api_key, search_engine_id, num_images)

    # Print image URLs
    if image_urls:
        for url in image_urls:
            return url
    else:
        return "No images found."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
