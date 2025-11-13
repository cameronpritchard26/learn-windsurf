# Python Hello World Web App

A simple Flask web application that echoes back user input.

## Features

- Single page web application
- Form with a text input field
- Displays the entered text back to the user with the message: "You entered this string: {userInput}"

## Requirements

- Python 3.x
- Flask 3.0.0

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python3 app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter any text in the input field and click "Submit" to see it echoed back.

## Project Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # HTML template with form
└── README_APP.md         # This file
```

## How It Works

1. The Flask app serves a single route (`/`) that handles both GET and POST requests
2. On GET request: displays the form
3. On POST request: captures the user input and displays it back on the same page
4. The template uses Jinja2 to conditionally display the result only after form submission
