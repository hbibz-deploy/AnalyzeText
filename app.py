from flask import Flask as App
from flask import render_template
from flask_socketio import SocketIO, send
from lib.Analyze import Analyze_factory as Af
from sys import argv as argument
import webbrowser
app = App(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

### Routes begin here

@app.route('/')
def home():
    return render_template('home.html')


### Routes for Errors

@app.errorhandler(404)
def page_not_found(e):
    return (render_template('404.html'), 404)


@socketio.on('message')
def handleMessage(msg):
    if 'connected' not in msg:
        result = Af(msg)
        send(result.run())


### Run

if __name__ == '__main__':
    if len(argument) > 1:
        if argument[1].upper() == "DEBUG":
            app.debug = True
            webbrowser.open_new("http://localhost:5000")
    socketio.run(app)
