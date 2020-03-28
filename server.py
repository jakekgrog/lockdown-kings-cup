from flask import Flask, render_template
from flask_socketio import SocketIO
from rules import rules
import json

from deck import Deck, Card

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
socketio = SocketIO(app)

connection_count = 0

global deck

deck = Deck()
deck.shuffle()

players = []
with open("players.txt", "r") as f:
    for line in f.readlines():
        players.append(line.strip().split())

global i
i = 0

global card
card = None

global player
player = ""

global alert
alert = ""

global kingcount
kingcount = 0

@socketio.on('onconnect')
def handle_onconnect(message):
    global connection_count
    global card
    global player
    global alert
    connection_count += 1
    socketio.emit('response', {"card": card.__str__(), "player": player, "alert": alert, "count": kingcount})

@socketio.on('pullcard')
def pullcard():
    global i
    global card
    global player
    global alert
    global kingcount
    global deck
    card = deck.pullCard()
    player = players[i]
    alert =  rules[card.value]
    i += 1

    if card.value == 13:
        kingcount += 1

    socketio.emit('response', {"card": card.__str__(), "player": player, "alert": alert, "count": kingcount})
    if i == len(players):
        i = 0
    if kingcount == 4:
        kingcount = 0
        deck = Deck()
        deck.shuffle()

@app.route('/')
def index():    
    if connection_count >= 15:
        print("REFUSED")
        return "error"
    return render_template("index.html")

if __name__ == '__main__':
    # Encapsulates the start up of the web server
    socketio.run(app, port="5000", host="0.0.0.0")