"""
Simple Flask Web Application for Learning Windsurf
This is a basic web app to demonstrate Windsurf's capabilities with Python development.
"""

from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Home page with welcome message."""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page with information about Windsurf."""
    return render_template('about.html')

@app.route('/api/time')
def get_time():
    """API endpoint that returns current server time."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        'time': current_time,
        'message': 'Current server time'
    })

@app.route('/api/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'windsurf-learning-app'
    })

if __name__ == '__main__':
    # NOTE: Debug mode is enabled for learning/development purposes.
    # In production, set debug=False and use a production WSGI server like gunicorn.
    # Example: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(debug=True, host='0.0.0.0', port=5000)
