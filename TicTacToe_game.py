import random

class Game:
    def __init__(self, size = 3):
        self.size = size

        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.empty_positions = []
        for r in range(size):
            for c in range(size):
                if self.board[r][c] == " ":
                    self.empty_positions.append((r, c))

    def perform_random_agent_move(self):
        row, col = random.choice(self.empty_positions)

        self.board[row][col] = "x"

        self.empty_positions.remove((row, col))

    def perform_random_rival_move(self):
            row, col = random.choice(self.empty_positions)
    
            self.board[row][col] = "o"
    
            self.empty_positions.remove((row, col))

    def check_win(self):
        #בודק שורות
        for i in range(self.size):
            first = self.board[i][0]
            if first != " " and all(self.board[i][j] == first for j in range(self.size)):
                return 1 if first == "X" else -1

        #בודק טורים
        for i in range(self.size):
            first = self.board[0][i]
            if first != " " and all(self.board[j][i] == first for j in range(self.size)):
                return 1 if first == "X" else -1

        #בודק אלכסון ראשי
        first = self.board[0][0]
        if first != " " and all(self.board[i][i] == first for i in range(self.size)):
            return 1 if first == "X" else -1

        #בודק אלכסון משני
        second = self.board[0][self.size-1]
        if second != " " and all(self.board[i][self.size-1-i] == second for i in range(self.size)):
            return 1 if second == "X" else -1

        if not self.empty_positions:
            return 0
        return 2
                
        
    def print_game_result(self):
        
        if self.check_win() == 1:
            return "x won !"      
        if self.check_win() == -1:
            return "o won !"
        if self.check_win() == 0:
            return "draw"

    def print_board(self):
        
        for i in range(self.size):
            col_str = "| " + " | ".join(self.board[i]) + " |" 
            print(col_str)

            if i < self.size - 1:
                print("-" * (self.size * 4 + 1))

    def cleanboard(self):
            
            self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
            self.empty_positions = []
            for r in range(self.size):
                for c in range(self.size):
                    if self.board[r][c] == " ":
                        self.empty_positions.append((r, c))

    def play(self):
        self.cleanboard()

        while self.check_win() == 2:

            mc = Monte_Carlo(self) 
            mc.simulations()

            self.perform_random_agent_move

            if self.check_win() != 2:
                return self.board, self.check_win()

            self.perform_random_rival_move

        return self.board, self.check_win()