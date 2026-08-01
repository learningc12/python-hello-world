from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from OpenShift!'

if __name__ == '__main__':
    # OpenShift routes traffic via port 8080 by default for non-root containers
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
