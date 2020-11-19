from app import app
from app.models.game_data import *
from flask import render_template

@app.route('/')
def home():
    return render_template("index.html", title="Rock Paper Scissors", players=players)

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1.choice = player_1_choice
    player_2.choice = player_2_choice
    winner = game.get_winner(player_1, player_2)
    return render_template("result.html", title = "The Result!", winner = winner)