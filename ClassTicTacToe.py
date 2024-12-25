class TicTacToe():
    def __init__(self, player: 1):
        assert 1 <= player and 2 >= player, f"Player must be 1 or 2"
        self.__curr_player = player
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__end = False
        self.__num_move = 0
        
        print(f"Player {self.__curr_player} goes first")
        self.PrintBoard()
        
        while self.__end == False:
            self.Move()
            
    def Check(self):
        for i in range(3):
            if self.__board[i][0] == self.__board[i][1] and self.__board[i][1] == self.__board[i][2]:
                return self.__board[i][0]
            elif self.__board[0][i] == self.__board[1][i] and self.__board[1][i] == self.__board[2][i]:
                return self.__board[0][i]
        
        if self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2]:
            return self.__board[0][0]
        
        if self.__board[2][0] == self.__board[1][1] and self.__board[1][1] == self.__board[0][2]:
            return self.__board[2][0]
        
        if self.__num_move == 9:
            return 3
        
        return 0
        
        
    
    def PrintBoard(self):
        for i in range(3):
            row = self.__board[i]
            print(row)
    
    def ValidMove(self, x_axis: int, y_axis: int):
        if x_axis < 0 or x_axis > 2 or y_axis < 0 or y_axis > 2:
            print(f"Wrong position, move again")
            return False
        elif self.__board[x_axis][y_axis] != 0:
            print(f"This position is occupied, move again")
            return False
        
        return True
         
        
    def Move(self):
        print(f"It's player {self.__curr_player}'s turn")
        
        valid = False
        while valid == False:
            x_axis = int(input("Enter value of x axis (an integer from 0 to 2): "))
            y_axis = int(input("Enter value of y axis (an integer from 0 to 2): "))
            valid = self.ValidMove(x_axis, y_axis)
       
        
        self.__board[x_axis][y_axis] = self.__curr_player
        self.__num_move += 1
            
        checker = self.Check()
        if checker != 0 and checker != 3:
            print(f"Player {checker} wins")
            self.__end = True
        elif checker == 0:
            self.__curr_player = 3 - self.__curr_player
            print(f"Player {self.__curr_player} goes next")
        else:
            print(f"Draw, game ends")
            self.__end = True
        
        #print the board after each move    
        self.PrintBoard()
            
