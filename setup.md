# Getting Started

This assumes that you are operating everything in VSCode. Modify and adapt accordingly if you do not use VSCode. 

## Setup the API keys

1. If you do not have one already, create a workspace specific `settings.json` in your directory. Inside it, put in the following:
```json
{
    "python.envFile": "${workspaceFolder}/.env"
}
```
2. Now, create a `.env` file in the main folder directory, not inside the `settings.json` file. 
3. Inside the `.env` file you'll need to insert the following attributes below. 
```env
GOOGLE_API_KEY=[INSERT VALUE HERE]
SEARCH_ENGINE_ID=[INSERT VALUE HERE]
CUSTOM_ENGINE_SEARCH_KEY=[INSERT VALUE HERE]
```
Note: The `GOOGLE_API_KEY` corresponds to the GEMINI API key. The `SEARCH_ENGINE_ID` is the custom search engine ID. The `CUSTOM_ENGINE_SEARCH_KEY` is another API key that you have to create seperately from the GEMINI API key. More instructions on creating such keys can be found in:
- [GEMINI API Key](https://ai.google.dev/tutorials/setup)
- [Custom search engine ID & API key](https://developers.google.com/custom-search/v1/overview)
4. Now you're all set up to run this repository locally on your machine!

## Setup on VSCode
To run this repository locally on your machine with VSCode, follow the instructions below.
0. Install python. There are many instructions online detailing how you can do this. 
1. Create a virtual environment in VSCode in the source directory. Type in the command palette: `Python: Create Environment...` and click on the `.venv` option when it presents itself. A new directory should appear on the folder sidebar with the name `.venv`. 
2. Next, activate the `.venv`. In the terminal, type in `python3 -m venv .venv`
3. Inside the terminal, there should now be a `(.venv)` on the very left side of every command. You are now in the virtual environment!

If you're having any issues with setting up a virtual environment, consult this resource: https://code.visualstudio.com/docs/python/environments
