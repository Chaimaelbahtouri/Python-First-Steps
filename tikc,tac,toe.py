import os
def clear_screen():
    os.system("cls")  #for windows#

class Users:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    def Check_name(self):
        while True:
            name = input("enter your name(letters only) : ")
            if name.isalpha():
                self.name = name
                break
            print("please Cheack your name ")
    def Check_symbol(self):
        while True:
            symbol = input(f"{self.name}, Enter a single letter  X or O : ").upper()
            if symbol.isalpha() and len(symbol) == 1:
                if symbol != "X" and symbol != "O":
                    print("Only X or O are allowed.")
                else:
                    self.symbol = symbol
                    break
            else:
                print("Invalid symbol. Please enter a single letter.")
                

class Menu:
    def Display_main_menu(self):
        print("welcome to Tic Tac Toe Game")
        print("1.Start Game")
        print("2.Quit Game")
        while True:
            choice = input("Enter your choice 1 or 2 : ")
            if choice == "1" or choice == "2":
                return choice
            else :
                print("invalid please check your choice")
    
    def Display_end_game(self):
        print("Game is over")
        print("1.Restart Game")
        print("2.Quit Game")
        while True:
            choice = input("Enter your choice 1 or 2 : ")
            if choice == "1" or choice == "2":
                return choice
            else :
                print("invalid please check your choice")
            
class Board:
    def __init__(self):
        self.board = [str(i)for i in range(1,10)]

    def Display_board(self):
        for i  in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6 : ##
                print("-"*5)
    def Update_board(self,choice,symbol):
        if self.Is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False

    def Is_valid_move(self,choice):
        return self.board[choice-1].isdigit() #SOLID Principles Single Responsibility Principle (SRP):
    def reset_board(self):
        self.board = [str(i)for i in range(1,10)]
class game:
    def __init__(self):
        self.players = [Users(),Users()]
        self.menu = Menu()
        self.board = Board()
        self.player_index = 0
    def Start_game(self):
        choice = self.menu.Display_main_menu()
        if choice == "1":
            clear_screen()
            self.set_up_player()
            self.Play_game()
        else:
            self.Quit_game()
            
    def set_up_player(self):
        for number, player in enumerate(self.players, start=1):  #search about this function in loop
            print(f"player{number}, Please enter your Details :")
            player.Check_name()
            player.Check_symbol()
            clear_screen()

    def Play_game(self):
        while True:
            self.turn_game()
            if self.check_win():
                print("Congratulations.you win")
                choice = self.menu.Display_end_game()
                if choice == "1":
                    self.restart_game()
                else:
                    self.Quit_game()
                    break
            elif self.check_draw():
                print("Draw!!")
                choice = self.menu.Display_end_game()
                if choice == "1":
                    self.restart_game()
                else:
                    self.Quit_game()
                    break


    
    def turn_game(self):
        player = self.players[self.player_index]
        self.board.Display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("enter between 1 and 9 : " ))
                if 1<=  cell_choice <= 9 and self.board.Update_board(cell_choice,player.symbol):
                    break
                else:
                    print("invalid move.try again") #if th cell is filled
            except ValueError :
                print("error. please choose between only 1 and 9") # if he does not enter between one and nin 1/9
        clear_screen()
        self.Switch()

    def Switch(self):
        self.player_index = 1 - self.player_index
    def check_win(self):
        win_comb = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
            ]
        for comb in win_comb:
            if (self.board.board[comb[0]] == self.board.board[comb[1]] == self.board.board[comb[2]]):
                return True
        return False
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
    
    def restart_game(self):
        self.board.reset_board()
        self.player_index = 0
        self.Play_game()
    
    def Quit_game(self):
        print("Thank you for your playing!!")