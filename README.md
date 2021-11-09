![[object Object]](https://socialify.git.ci/Deepak-Perla/RASA-BOT/image?font=Inter&language=1&name=1&owner=1&pattern=Floating%20Cogs&theme=Dark)

# RASA Hotel Chatbot
A simple chatbot using Rasa.

# About
The chatbot responds to and handle the following basic functionalities
- Booking room by giving the place and dates.
- It optionally asks the location(like near "Buckingham Palace" "Near to park")
- It gives links to you to book directly

# Requirements
`python 3.6.8` is used for this project and use a fresh virtual environment for installing all dependencies.
```bash
(venv)  pip install -r requirements.txt
```

# Usage
Train the chatbot
```bash
rasa train
```
Run actions.py in another terminal and keep it running
```bash
rasa run actions
```
Use the chatbot after training as
```bash
rasa shell
```
To run chatbot in localhost
```bash
rasa run -m models --enable-api --cors "*"
```
