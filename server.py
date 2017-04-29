from __future__ import print_function
from flask import Flask, render_template
from flask_socketio import SocketIO
import sys
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


from flask_socketio import send, emit

@socketio.on('message')
def handle_message(message):
    print(message, file=sys.stderr)
    send(message)


@app.route('/')
def index():
    return render_template("hotel.html")
s
# app.run(port="8080")
if __name__ == '__main__':
    socketio.run(app)

