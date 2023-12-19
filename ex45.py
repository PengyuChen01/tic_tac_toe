from random import randint
from sys import exit
class tic_tac_toe(object):
    def enter(self):
        print("""Welcome to tic_tac_toe game, it's a simple game, first person get 3 in a row wins 
              Circle for Player and Cross for bot. Now please choose you want to start first (1) or let bot start first(0)""")
        choice = input("< ")
        if choice == 0:
            return mark.player_mark()
        elif choice == 1:
            return mark.bot_mark()
        else:
            print("invalid option, can you READ?")
            tic_tac_toe()
        return Play()

# draw the grid and update the grid
class Grid():
    def __init__(self, grid):
        self.grid = grid
        grid = [["-" for i in range (3)] for j in range(3)]
    def update_grid(self, updated_row, updated_column):
        if player == "bot":
            self.grid[updated_row][updated_column] == 'X'
        else:
            self.grid[updated_row][updated_column] == 'O'    
    def player_mark_position(self):
        print("please enter row , column for placing circle")
        row,column = [int(x) for x in input("Enter row and columns: ").split(",")]
        self.update_grid(self,row -1,column - 1)
    # randomly generate row and column from 0-2
    def bot_mark_position(self,player):
        row,column = randint(0,2),randint(0,2)

# end game condition
class Play(tic_tac_toe,mark):
    def play(self, grid, player):
        while grid has '-':
            if tic_tac_toe.enter.choice == 0:
                # to-do no duplicate for marked thing
                mark.player_mark(0)
                mark.bot_mark(1)
            else:
                mark.bot_mark(1)
                mark.player_mark(0)
        return end()
class end():
    def __init__(self,grid):
        self.grid = grid
    
    def win(self):
        if self.grid[0] == 'O' and self.grid[1] == 'O' and self.grid[2] == 'O' or self.grid[0] == 'O' and self.grid[3] == 'O' and self.grid[6] == 'O' or  self.grid[2] == 'O' and self.grid[5] == 'O' and self.grid[8] == 'O' or self.grid[6] == 'O' and self.grid[7] == 'O' and self.grid[8] == 'O' or self.grid[2] == 'O' and self.grid[4] == 'O' and self.grid[6] == 'O':
            print(" Congrates you win the game")
        else:
            print(" you lose the game!")
            exit(1)

        


a = tic_tac_toe()
a.enter()





#grid : 1 - 9 2d array
#win fullfill all the grid and one player has either 012,036,258,678,246
#lose doesn't meet win condition
#play player and ai take turn. 

