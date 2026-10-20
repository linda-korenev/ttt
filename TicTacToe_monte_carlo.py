from TicTacToe_game import *
import csv
import copy
import os

class Monte_Carlo:
    def __init__(self, game: Game):
        self.size = game.size 
        self.board = copy.deepcopy(game.board) 
        self.available_positions = copy.deepcopy(game.available_positions) 
        self.moves_scores = {} 

    def board_to_arr_mc(self, board):
        mapping = {'x': 1, 'o': -1, ' ': 0}  
        arr = [] 
        positions_order = [(0, 0),(1, 0),(2, 0),(0, 1),(1, 1),(2, 1),(0, 2),(1, 2),(2, 2)] 
        for r, c in positions_order: 
            arr.append(mapping[board[r][c]]) 
        return arr 

    def run_simulations(self):
        for start_pos in self.available_positions: 
            sim_game = Game(size=self.size) 
            sim_game.board = copy.deepcopy(self.board) 
            sim_game.available_positions = copy.deepcopy(self.available_positions) 

            sim_game.available_positions.remove(start_pos) 
            r, c = start_pos 
            sim_game.board[r][c] = 'x' 

            initial_board = copy.deepcopy(sim_game.board) 

            
            while sim_game.check_win() == 2:
                sim_game.perform_rival_move()
                if sim_game.check_win() != 2:
                    break
                sim_game.perform_agent_move()

            result = sim_game.check_win() 

            self.moves_scores[start_pos] = {'board': initial_board,'score': result} 

        self.save_to_csv() 

    def save_to_csv(self, filename='monte_carlo_results.csv'):
        db = {} 

        
        if os.path.exists(filename):
            with open(filename, mode='r', newline='', encoding='utf-8') as f: 
                reader = csv.reader(f)
                next(reader) 
                for row in reader:
                    key = tuple(row[:9]) 
                    db[key] = float(row[9])

    
        for data in self.moves_scores.values(): 
            arr = self.board_to_arr_mc(data['board']) 
            key = tuple(map(str, arr)) 

            calculated_score = data['score'] / 100000.0

            
            if key in db: 
                db[key] += calculated_score
            else:
                db[key] = calculated_score

    
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['(0,0)','(1,0)','(2,0)','(0,1)','(1,1)','(2,1)','(0,2)','(1,2)','(2,2)','score'])
            for key, score in db.items(): 
                writer.writerow(list(key) + [score])