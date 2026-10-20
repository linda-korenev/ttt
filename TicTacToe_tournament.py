from TicTacToe_game import *
import csv
import os

class Tournament:
    def __init__(self, game: Game, csv_filename='tournament_results.csv'):
        self.game = game 
        self.csv_filename = csv_filename 
        self.stats = {1: 0, -1: 0, 0: 0} 

    def board_to_arr(self, board):
        mapping = {'x': 1, 'o': -1, ' ': 0}  
        arr = [] 
        positions_order = [(0, 0),(1, 0),(2, 0),(0, 1),(1, 1),(2, 1),(0, 2),(1, 2),(2, 2)] 
        for r, c in positions_order: 
            arr.append(mapping[board[r][c]])
        return arr 

    def _prepare_row(self, final_board, result):
        row_data = self.board_to_arr(final_board)
        # הופך 0 (תיקו) ל-2 עבור שורת התוצאה
        if result == 0:
            result_game = 2
        else:
            result_game = result
            
        row_data.append(result_game)
        return row_data

    def _save_to_csv(self, rows_buffer):
        file_exists = os.path.exists(self.csv_filename)

        with open(self.csv_filename, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow('(0,0)','(1,0)','(2,0)','(0,1)','(1,1)','(2,1)','(0,2)','(1,2)','(2,2)','result')
            writer.writerows(rows_buffer)
    
    def play_games(self, count): 
        rows_buffer = []

        for i in range(0, count): 
            final_board, result = self.game.play() 

            self.stats[result] += 1

            row_data = self._prepare_row(final_board, result)
            rows_buffer.append(row_data)

        self._save_to_csv(rows_buffer)

        self.print_tournament_results()
            
    def print_tournament_results(self):
        print('=== סיכום הטורניר ===') 
        print(f'ניצחונות (X): {self.stats[1]}') 
        print(f'הפסדים (O): {self.stats[-1]}') 
        print(f'תיקו: {self.stats[0]}') 

