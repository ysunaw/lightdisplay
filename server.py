from __future__ import print_function
from flask import Flask, render_template
from flask_socketio import SocketIO
import sys
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


from flask_socketio import send, emit
from os import environ
from flask import Flask
#haha

#app.run(environ.get('PORT'))

@socketio.on('message')
def handle_message(message):
    print(message, file=sys.stderr)
    send(message)


@app.route('/')
def index():
    return render_template("hotel.html")
# app.run(port="8080")
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT','5000'))
    except ValueError:
        PORT = 5000
#    app.run(HOST, PORT)
    socketio.run(app, port =  PORT, host= HOST)

