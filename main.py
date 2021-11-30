
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_pymongo import PyMongo

app = Flask(__name__)
# enable encryption
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# mongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
socketio = SocketIO(app)


@app.route('/')
@app.route('/<room_name>')
def sessions(room_name=None):
    return render_template('session.html', room_name=room_name)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
