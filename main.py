from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    # more stuff here
    return "<p>Hello, world!</p>"

if __name__ == '__main__':
    # load environment variables from .env file
    load_dotenv()

    # access the API key from environment variables
    gemini_api_key = os.getenv("GOOGLE_API_KEY")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    custom_search_engine_api_key = os.getenv("CUSTOM_ENGINE_SEARCH_KEY")
    app.run(debug=True, host='0.0.0.0', port=8000)
