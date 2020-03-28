from flask import Flask, render_template
from flask_socketio import SocketIO
import json

from deck import Deck, Card

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
socketio = SocketIO(app)

connection_count = 0

deck = Deck()
deck.shuffle()

players = ["Jake", "Jack", "Alina", "Greta", "Cormac", "Eoghan", "Sophie", "Aaisha", "Sean", "Leah", "Carrie"]
global i
i = 0

@socketio.on('onconnect')
def handle_onconnect(message):
	global connection_count
	connection_count += 1
	print(message)

@socketio.on('pullcard')
def handle_skip():
    global i
    card = deck.pullCard()
    print(card)
    i += 1
    socketio.emit('response', {"card": card.__str__(), "player": players[i]})
    if i == len(players) - 1:
        i = 0
    return 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
	if connection_count >= 15:
		print("REFUSED")
		return "error.html"
	return render_template("game.html")

if __name__ == '__main__':
    # Encapsulates the start up of the web server
    socketio.run(app, port="5000", host="0.0.0.0")