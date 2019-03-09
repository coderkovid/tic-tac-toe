from main_game import TicTacToe

game = TicTacToe()

for i in range(10):
	x = int(input("Enter the square: "))
	game.move(x)
