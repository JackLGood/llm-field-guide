# llm-field-guide

## Setup
### Python Virtual Environment
If you'd like, setup a virtual environment as follows:
```
> python -m venv testing-env
```
To activate the virtual environment on Windows: 
```
> .\testing-env\Scripts\activate
```
On Mac and Unix:
```
> source testing-env\bin\activate
```
### Install Python libraries
General Python libraries:
```
> pip install python-dotenv
```
Libraries for dealing with sound recording and playback:
```
> pip install playsound == 1.2.2
> pip install sounddevice
> pip install scipy
```
Libraries for marker recognition with OpenCV:
```
pip install opencv2
```
LLM libraries for Python:
```
> pip install --upgrade openai
```
### Add API Key
Set it the API keys by creating a `.env` file in the project folder (e.g. chatgpt-test). Copy the text below (replacing your API key) into the `.env` file.
```
# Krithik's API Key
OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxx
```
