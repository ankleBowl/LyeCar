from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

class ThreadedEmitter:
    def __init__(self, socketio):
        self._socketio = socketio

    def send(self, message):
        self._socketio.send(message)

import serial
from serial.tools import list_ports

class Arduino(ThreadedEmitter):
    def __init__(self, socketio, serial_port, baud_rate):
        super().__init__(socketio)
        self._serial_port = serial_port
        self._baud_rate = baud_rate

        # print all serial devices


    def start(self):
        for port in list_ports.comports():
            print(port)
        pass

threaded_modules = [
    Arduino(socketio, '/dev/ttyACM0', 9600)
]

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    socketio.send('Received: ' + msg)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

for module in threaded_modules:
    module.start()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000)