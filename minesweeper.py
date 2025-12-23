import random


class board:
    def __init__(self,length):
        self.length = length
        self.board = [[0] * length for _ in range(length)]

    def add_mines(self,const):
        for i in range(self.length):
            for k in range(self.length):
                
                a = random.randint(0,100)
       
       
            
                
                
                
                if a>const:
                    self.board[i][k]= 'n'
        
    def display(self):
        for i in range(self.length):
            print(self.board[i])

class answer_board():
    def __init__(self,board):
        for i in range(board.length):
            for j in range(board.length):
                if board.board[i][j] == 'n':
                    for k in range(3):
                        for l in range(3):
                            a = i+k-1
                            b = j+l-1
                            print(a,b)
                            if a >=0 and a <=9 and b>=0 and b<=9:
                                if board.board[a][b] != 'n':
                                    board.board[a][b]+=1
        
                    
                            
                            
                            
                
            

    
class game_board():
    def __init__(self,board_real):
        self.answer_board = board_real
        self.length =board_real.length
        self.board = [['?'] * self.length for _ in range(self.length)]
        
    def display(self):
        for i in range(self.length):
            print(self.board[i])

            
class game:
    def __init__(self):
        self.je = board(10)


        self.je.add_mines(80)
        self.je.display()

        self.ga = game_board(self.je)
        self.ga.display()
        a = answer_board(self.je)
    def process(self):
        x = int(input('x:'))
        y = int(input('y:'))
        print(self.je.board[x][y])
        





game = game()
while True:
    game.process()

