# baby hangman
# reading from file tho
# 19 June 19

import random

filename = 'wordlist_10000.txt'
hangman_ascii = ['''
 +---+
     |
     |
     |
     ===''', '''
 +---+
 O   |
     |
     |
     ===''', '''
 +---+
 O   |
 |   |
     |
     ===''', '''
 +---+
 O   |
/|   |
     |
     ===''', '''
 +---+
 O   |
/|\\  |
     |
     ===''', '''
 +---+
 O   |
/|\\  |
/    |
     ===''', '''
 +---+
 O   |
/|\\  |
/ \\  |
     ===''']

def get_random_word(file):
	with open(file) as f_obj:
		lines = f_obj.readlines()	# store in list

	index = random.randint(0, len(lines) - 1)
	mysteryword = lines[index]
	return mysteryword.rstrip()		# VERY IMPORTANT OR YOU'LL GET A BLANK

def display_board(missed_letters, correct_letters, mystery_word, ascii_array, already_guessed):
	print(ascii_array[len(missed_letters)] + '\n')

	blanks = '_' * len(mystery_word)

	# replace blanks with correct letters
	for i in range(len(mystery_word)):	
		if mystery_word[i] in correct_letters:
			blanks = blanks[:i] + mystery_word[i].upper() + blanks[i + 1:]

	# show secret word w spaces in between
	for letter in blanks:	 
		print(letter,end='')

	print("\n\nMissed letters: ", end='')
	for letter in sorted(missed_letters):
		print(letter.upper(), end=' ')
	print()

def get_guess(already_guessed):
	"""Returns letter player entered, makes sure player enters single letter"""
	while True:
		guess = input("\nGuess a letter. ")
		guess = guess.lower()
		if len(guess) != 1:
			print("Enter a single letter.")
		elif guess in already_guessed:
			print("You already guessed this letter.")
		elif guess.isalpha() == False:
			print("Invalid -- Enter a letter.")
		else:
			already_guessed.append(guess)
			return guess

def play_again():
	answer = input("Do you want to play again? Y / N   ")
	return answer.lower().startswith('y')

print("\nH A N G M A N")	
missed_letters = ''
correct_letters = ''
already_guessed = []
mystery_word = get_random_word(filename)
game_is_done = False

while True:
	display_board(missed_letters,correct_letters,mystery_word,hangman_ascii,already_guessed)

	# player enters letter
	guess = get_guess(already_guessed)

	# if letter in word
	if guess in mystery_word:
		correct_letters += guess

		# check if player has won
		found_all_letters = True
		for i in range(len(mystery_word)):
			# if a letter hasn't been uncovered
			if mystery_word[i] not in correct_letters:
				found_all_letters = False
				break
		if found_all_letters:
			print(f"\nYeah!! The secret word is {mystery_word.upper()}. Winner!\n")
			game_is_done = True
	# if letter not in word
	else:
		missed_letters += guess

		# check if loser
		if len(missed_letters) == len(hangman_ascii) - 1:
			display_board(missed_letters,correct_letters,mystery_word,hangman_ascii,already_guessed)
			print(f"\nOut of guesses! RIP. The correct word was {mystery_word.upper()}.\n")
			game_is_done = True

	# ask if replay if game is done
	if game_is_done:
		if play_again():
			missed_letters = ""
			correct_letters = ""
			already_guessed = []
			game_is_done = False
			mystery_word = get_random_word(filename)
		else:
			break