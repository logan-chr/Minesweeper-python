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
                    self.board[i][k]= 1
        
    def display(self):
        for i in range(self.length):
            print(self.board[i])
        

    
class game_board():
    def __init__(self,board_real):
        self.answer_board = board_real
        self.length =board_real.length
        self.board = [['?'] * self.length for _ in range(self.length)]
        
    def display(self):
        for i in range(self.length):
            print(self.board[i])
            
class gameg
        
je = board(10)


je.add_mines(80)
je.display()

ga = game_board(je)
ga.display()



