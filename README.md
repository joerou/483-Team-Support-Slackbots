# 483-Team-Support-Slackbots

## Development platform
I am using Ubuntu(WSL2) and VSCode as editor. \
The commend list here should work on any Linux machine. 

## Set up Python environment:

We're using venv (or virtualenv) to keep the dependencies and environmental variables specific to this app. See venv docs for more info.
```python
python3 -m venv env
```
Then initialize the virtualenv:
```python
source env/bin/activate
```
Install the app's dependencies:
```python
pip install -r requirements.txt
```
Copy your app's Bot User OAuth Access Token and add it to your python environmental variables
```
export SLACK_BOT_TOKEN=xoxb-111-222-xxxXXxxXXxXXxXXXXxxxX
```
Add your app's Signing Secret to your python environmental variables
```
export SLACK_SIGNING_SECRET=xxxxxxxxXxxXxxXxXXXxxXxxx
```

Reference: https://github.com/slackapi/python-slack-events-api/blob/main/example/README.rst