from flask import Flask
import os

app = Flask(__name__)

# Get the port from the environment variable or default to 8000
port = int(os.environ.get('PORT', 8000))

@app.route('/')
def index():
    return 'Hello user.'

if __name__ == '__main__':
    # Run the app on all available IPs (0.0.0.0) and the specified port
    app.run(host='0.0.0.0', port=port)
