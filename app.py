from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    pod_name = os.getenv('POD_NAME', 'Unknown Pod')
    node_name = os.getenv('NODE_NAME', 'Unsknown Node')
    namespace = os.getenv('NAMESPACE', 'Unknown Namespace')

    return f"Container EDU | POD Working : {pod_name} | nodename : {node_name} | namespace : {namespace}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
