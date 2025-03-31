# Practising to create server following the lesson of topic 6
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello there"

@app.route('/blah2')
def blah():
        return "this is blah2"

if __name__ == "__main__":
    app.run(debug = True)
    
# Run de program with python to get the url