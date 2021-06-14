from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello world!'

@app.route('/SubmitRequest/FriendRequest', methods=['POST'])
def checkPost():
    return 'This is function which sends a friend request'
