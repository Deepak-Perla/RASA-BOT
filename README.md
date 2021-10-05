![](https://socialify.git.ci/Deepak-Perla/RASA-BOT/image?description=1&descriptionEditable=An%20Interactive%20Chatbot%20made%20using%20RASA%20Framework%E2%9A%99%EF%B8%8F%E2%9A%99%EF%B8%8F%E2%9A%99%EF%B8%8F&font=Inter&language=1&logo=https%3A%2F%2Fwww.linkpicture.com%2Fq%2Fprofile-pic_5.png&owner=1&pattern=Floating%20Cogs&theme=Dark)

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
