from flask import Flask, jsonify, request, Response
from dotenv import load_dotenv
import os
import requests
import json

app = Flask(__name__)

@app.route('/')
def default():
    return "<p>Hello world!</p>"

@app.route('/api/generate_itinerary')
def generate_itinerary():
    # these are REQUIRED parameters!
    time_of_visit = request.args.get('time_of_visit')
    list_to_visit = request.args.get('list_to_visit')

    # get the GEMINI API key
    gemini_api_key = os.getenv('GOOGLE_API_KEY')

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={gemini_api_key}"
    headers = {'Content-Type' : 'application/json'}
    
    # modify the prompt here!
    prompt = "generate an travel itinerary that includes all of the following list " + list_to_visit + "in " + time_of_visit +"days"
    # ask it to format the json
    prompt += "Please provide a response in a structured JSON format that matches the following model: [{Day: day number, morning: [morning activities (do not include optional)], afternoon: [afternoon activities (do not include optional)], evening: [evening activities (do not include optional)]}]"

    data = {
        'contents': [
            {
                "role": "user",
                'parts': [{
                    "text": prompt,
                }]
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json",
        }
    }

    response = requests.post(url, headers=headers, json=data)
    json_text = get_gemini_response_text(response.json())

    return jsonify(json_text)

@app.route('/api/transportation')
def get_transportation():
    # list required parameters
    to_city = request.args.get('to_city')
    from_city = request.args.get('from_city')
    transportation_method = request.args.get('transportation_method')
    time_of_visit = request.args.get('time_of_visit')

    # get the GEMINI API key
    gemini_api_key = os.getenv('GOOGLE_API_KEY')

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={gemini_api_key}"
    headers = {'Content-Type' : 'application/json'}


    prompt = "provide ONLY a number for ticket price for round-trip " + transportation_method + "from" + from_city + " to " + to_city + " during "+ time_of_visit
    prompt += "Please provide a response in a structured JSON format that matches the following model: [ budget: budget ]"
    
    data = {
        'contents': [
            {
                "role": "user",
                'parts': [{
                    "text": prompt,
                }]
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json",
        }
    }

    response = requests.post(url, headers=headers, json=data)
    json_text = get_gemini_response_text(response.json())

    return jsonify(json_text)

@app.route('/api/daily_transportation')
def get_daily_transportation():
    # list required parameters following this example
    city_name = request.args.get('city_name')

    # get the GEMINI API key
    gemini_api_key = os.getenv('GOOGLE_API_KEY')

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={gemini_api_key}"
    headers = {'Content-Type' : 'application/json'}


    prompt = "Estimate A singular number of budget of ground transportation traveling in " + city_name + ". Please provide a response in a structured JSON format that matches the following model: [ tranportation price: transportation price ]"
    
    data = {
        'contents': [
            {
                "role": "user",
                'parts': [{
                    "text": prompt,
                }]
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json",
        }
    }

    response = requests.post(url, headers=headers, json=data)
    json_text = get_gemini_response_text(response.json())

    return jsonify(json_text)
    

# helper function for feeling_lucky()
def get_gemini_response_text(json_obj):
    return json_obj['candidates'][0]['content']['parts'][0]['text']

# was testing for retrieving image URLs of the cities
@app.route('/api/test')
def test():
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

@app.route('/api/city_image')
def city_image():
    # REQUIRED argument!
    city_name = request.args.get('city_name')
    return jsonify(get_image_url(city_name, 1))

# generates a list of cities to look at if they are interested
@app.route('/api/lucky')
def feeling_lucky():
    # these are REQUIRED parameters!
    travel_style = request.args.get('travel_style')
    country = request.args.get('country')

    # get the GEMINI API key
    gemini_api_key = os.getenv('GOOGLE_API_KEY')

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={gemini_api_key}"
    headers = {'Content-Type' : 'application/json'}

    # create the prompt
    generate_cities_and_description_prompt = "You are an amazing and well known traveling advisor. Generate a list of tourist CITIES in " + country + " that are " + travel_style
    generate_cities_and_description_prompt += ". Also, make sure to add a one sentence desciption to the following list of cities and add desciption for each of them for travelers"
    # ask it to format the json
    generate_cities_and_description_prompt += "Please provide a response in a structured JSON format that matches the following model: [{city: city name, description: desciption}]"

    data = {
        'contents': [
            {
                "role": "user",
                'parts': [{
                    "text": generate_cities_and_description_prompt,
                }]
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json",
        }
    }

    response = requests.post(url, headers=headers, json=data)
    json_text = get_gemini_response_text(response.json())

    # now populate the google images
    cities = json.loads(json_text)
    for city in cities:
        city_name = city["city"]
        city_image_url = get_image_url(city_name, 1)
        # add the city image url to the dictionary
        city["image_url"] = city_image_url
    
    # cities should be a text, seems like jsonify doesn't support dicts
    cities_text = json.dumps(cities, ensure_ascii=False)

    return jsonify(cities_text)

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
