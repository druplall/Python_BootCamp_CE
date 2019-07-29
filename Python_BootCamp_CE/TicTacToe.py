# Attempt at coding tic tac toe
# The game will be designed with two player 
# The grid will be the following 
# 7 8 9
# 4 5 6
# 1 2 3 

Player1 = None
Player2 = None

print("Welcome to Deo Tic Tac Toe !")
print("############################")

Player1 = input("Player 1: Do you want to be X or O ? ")
if(str(Player1) == 'X'):
    print("Player 1 will go first.")
    Player2 = 'O'
else:
    print("Player 1 is O and Player 2 will go first.")
    Player2 = 'X'
