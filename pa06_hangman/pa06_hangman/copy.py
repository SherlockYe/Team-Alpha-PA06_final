want_to_play = True
while (want_to_play):
	guessed_letters = []
	guesses_left = 6
	word= random.choice(words)
	print('I am thinking a word of ',len(word),'letters long')
	letter = input('Please choose a letter')
	letter=letter.lower()
	done = False
	correct_letters=''
	missed_letters=''
	while not done:
		if letter in guessed_letters:
			guesses_left-=1 ##subtract one from guesses_left
			print('You just guessed',letter)##and tell them they already guessed that letter
			print('And now you have',guesses_left,'chances left')
		elif letter not in word:
			guessed_letters.append(letter)##add letter to guessed letters
			print('Sorry, the letter you guessed is not in the word')#tell user the letter is not in the word
			guesses_left-=1##subtract one from the guesses_left
			print('And now you have ',guesses_left,'chances left')
		else:
			guessed_letters.append(letter)##add letter to guessed letters
			print('Congrats!! The letter you guessed is in the word')##tell user the letter is in the word
		if letter in word:
			correct_letters=correct_letters+letter
			get_all_letters=True
			for i in range(len(word)):
				if word[i] not in correct_letters:
					get_all_letters=False
					break
			if get_all_letters: ##all the letters in the word have been guessed
				print('Congrats!! You found the word!! The word is',word)
				want_to_play=False ##set done to be true and tell the user they won!
				break
		else:
			missed_letters=missed_letters+letter
		if guesses_left==0:##the number of guesses left is zero
			print('Sorry, you have used up all your attempts. You lost.The word I am thinking is', word)
			want_to_play=False ##set done to be true and tell the user they lost!
			break
		else:
			print_word(word, guessed_letters)##print the word with a dash for each letter not in guessed_letters
			letter =input('Please enter another letter.') ##ask the user for another letter
			print(guessed_letters)
	want_to_play = input('Do you want to play another game? Y/N')##ask the user if they want to play another game...
	if want_to_play=='Y':
		continue
	else:
		break
global state
if request.method == 'GET':
	return play()
