from __future__ import print_function
from flask import Flask, render_template,request
from flask_socketio import SocketIO
import sys
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from flask_socketio import send, emit
from os import environ
from flask import Flask
#app.run(environ.get('PORT'))

@socketio.on('message')
def handle_message(message):
	print(message, file=sys.stderr)
	send(message)
@app.route('/api/mode')
def api_mode():
	print("request",file = sys.stderr)
	print (request,file = sys.stderr)
	mode = request.args.get('mode')
	print (mode, file = sys.stderr)

	socketio.emit('api_mode',{'mode': mode})
	return render_template("hotel.html")

@app.route('/api/facility')
def api_facility():
	print("request",file = sys.stderr)
	print (request,file = sys.stderr)
	action = request.args.get('action')
	facility = request.args.get('facility')
	print (action, file = sys.stderr)

	socketio.emit('api_facility',{'action': action, 'facility' : facility})
	return render_template("hotel.html")

@app.route('/')
def index():
	return render_template("hotel.html")
# app.run(port="8080")
if __name__ == '__main__':
	HOST = environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(environ.get('PORT','5009'))
	except ValueError:
		PORT = 5009
#    app.run(HOST, PORT)
	socketio.run(app, port =  PORT, host= '0.0.0.0')
