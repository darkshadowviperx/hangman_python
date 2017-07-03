import os
import csv
import random

won = None
max_guess = None
secret_word = None
secret_word_arr = None
board = None

def set_up_game():
	global won
	global max_guess
	global secret_word
	global board
	
	won = False
	max_guess = 8
	secret_word = None
	board = []
	load_word()
	init_board()
	
def print_hangman(num_stages):
	stages = ["", "________ ", "| ", "|  | ", "|  0 ", "| /|\ ", "| / \ ", "| " ]
	for i in range(0,num_stages):
		print(stages[i])

def load_word():
	global secret_word
	global secret_word_arr
	
	words = None
	with open(os.path.join( os.environ['HOME'], 'Documents', 'hangman', 'word_list.txt')) as f:
		words = f.read().strip().split("\n")
	secret_word = words[random.randint(0,len(words) -1 )].strip()
	secret_word_arr = list(secret_word)
		
def init_board():
	global secret_word
	global board
	for i in range(0, len(secret_word)):
		board.append("_")
	
def play():
	global won
	global max_guess
	global secret_word
	global board
	
	print("Welcome to Hangman")
	
	while True:
		set_up_game()
		num_guess = 0
		
		while num_guess <= max_guess:
			print_hangman(num_guess)
			print_board()
			user_put = input('Guess a letter: ').lower()
			
			if user_put in secret_word_arr:
				temp_dex = secret_word_arr.index(user_put)
				board[temp_dex] = secret_word[temp_dex]
				secret_word_arr[temp_dex] = '*'
				
				if '_' not in board:
					won = True
					break
			else:
				print("{} not in secret_word".format(user_put) )				
				num_guess += 1
		
		if won:
			print("\n")
			print_board()
			print("Congratulations you win!\n")
		else:
			print("\nGame Over! \nWord was {}. \nBetter luck next time!\n".format(secret_word))
		
		if input("Do you want to play again? Type y: ").lower() != 'y':
			break
	
	print("Thanks for playing " + os.environ['USER'] + '!')
	
def print_board():
	global board
	temp = ''
	for letters in board:
		temp = temp + letters + ' '
	print(temp)
	