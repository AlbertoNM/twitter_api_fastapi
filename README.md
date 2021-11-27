# Twitter API in FastAPI
Twitter API clone made for learning purposes. The project uses FastAPI classes and Pyndantic models to simulate the Twitter API.

The interactive documentation of the API with Swagger UI is available at: `{localhost}/docs`.

##Content
* main.py
* The requirements
* Script in bash (use a bash shell to run the script)
* 2 .json files 

## API usage
First clone the repository in a directory and install the requirements creating a virtual environment.
```Shell
python3 -m venv venv
```
>Note: The name of the virtual environment is venv because bash script use this name to run

Initiates the environment.
```Shell
source venv/bin/activate
```
If you are in windows you need to type:
```Shell
.\venv\Scripts\activate
```
Then install the API requirements, the repository have the requirements in requirements.txt
```Shell
pip install -r requirements.txt
```
And finally you can use the script to start the service.
```Shell
source start.sh
```
>It is important that you start the script in the project directory because the script creates the json files, you will need them to do some API operations.
The script can start the environment for you. You do not need to start the environment manually in the shell