from TicTacToe_game import *
from TicTacToe_tournament import *
if __name__ == "__main__":
    game = Game()
    tournament = Tournament(game) 
    rounds = input("How many rounds?")
    tournament.play_games(int(rounds))