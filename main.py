
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
from flask_pymongo import PyMongo

app = Flask(__name__)
# enable encryption
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# mongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/chatbase"
socketio = SocketIO(app)
mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    online_users = mongo.db.users.find({"online": True})
    print(request.method)
    if request.method == 'POST':
        if request.form.get('search') == 'Search/Create':
            # pass
            room_name = request.form.get('roomName')
            print(room_name)
            return redirect(url_for("room", room_name=room_name))
        else:
            # pass # unknown
            return render_template("index.html",
                                   online_users=online_users)
    elif request.method == 'GET':
        print("No Post Back Call")

    return render_template("index.html",
                           online_users=online_users)


@app.route('/room/<room_name>', methods=['GET', 'POST'])
def room(room_name=None):
    return render_template('session.html', room_name=room_name)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
