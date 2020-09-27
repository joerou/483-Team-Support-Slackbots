## 483-Team-Support-Slackbots

# Development platform
I am using Ubuntu(WSL2) and VSCode as editor. 
The commend list here should work on any Linux machine. 

# Set up Python environment:

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