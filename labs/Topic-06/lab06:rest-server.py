# Create an application server that will implement a RESTful API.
# The API should allow a user to perform CRUD operations on an entity (eg a book)
# Test it using CURL

# very simple flask server

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"
    
# getall
# curl http://127.0.0.1:5000/books

@app.route('/books', methods=['GET'])
def getall():
        return "get all"

# find by id
# curl http://127.0.0.1:5000/books/1

#create
#curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json

        return f"create {jsonstring}"
    
# update
# curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        return f"update {id} {jsonstring}"
    
# Delete
# curl -X DELETE  http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
        return f"delete {id}"
    
if __name__ == '__main__':
    app.run(debug=True)