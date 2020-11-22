from app import app
from app.models.game_data import *
from flask import render_template, request, redirect

@app.route('/')
def home():
    return render_template("index.html", title="Rock Paper Scissors")

@app.route('/welcome')
def welcome():
    return render_template("welcome.html", title="Rock Paper Scissors", players=players)

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    winner = game.get_winner(player_1, player_2)
    return render_template("result.html", title = "The Result!", winner = winner)

@app.route('/create-players')
def create_players():
    return render_template("create_players.html", title="Rock Paper Scissors")

@app.route('/add-players', methods=["POST"])
def add_players():
    print(request.form)
    player_1.name = request.form["player_1_name"]
    player_1.choice = request.form["player_1_choice"]
    player_2.name = request.form["player_2_name"]
    player_2.choice = request.form["player_2_choice"]
    return redirect('/welcome')

@app.route('/play-computer')
def play_computer():
    return render_template("play-computer.html", title="Rock Paper Scissors")

@app.route('/add-player-vs-computer', methods=["POST"])
def add_player_vs_computer():
    print(request.form)
    return "Done"