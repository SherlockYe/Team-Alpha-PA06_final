"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':" ",
		 'word_so_far':"-----------",
		 'done':False,
		 'message':" ",
         'correct_letters':" "}

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
	global state
	state['word']=hangman_app.generate_random_word()
	state['guesses'] = []
	word_so_far = hangman_app.get_word_so_far(state['word'])
	state['word_so_far'] = word_so_far
	print(state)
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return start()
	elif request.method == 'POST':
		letter = request.form['guess']
		if letter in state['guesses']:
			state['message'] = 'You just guessed ' + letter##and t ell them they already guessed that letter
		elif letter not in state['word']:
			state['guesses'] += letter##add letter to guessed letters
			state['message'] = 'Sorry, the letter you guessed is not in the word'#tell user the letter is not in the word
		else:
			state['guesses'] += letter##add letter to guessed letters
			state['message'] = 'Congrats!! The letter you guessed is in the word'# check if letter has already been guessed
		if letter in state['word']:
			state['correct_letters'] += letter
			get_all_letters=True
			for i in range(len(state['word'])):
				if state['word'][i] not in state['correct_letters']:
					get_all_letters=False
					break
			if get_all_letters: ##all the letters in the word have been guessed
				state['message'] = 'Congrats!! You found the word!! The word is '+ state['word']
# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them
		#state['guesses'] += [letter]
		state['word_so_far'] = hangman_app.print_result(state['word'],state['guesses'])
		return render_template('play.html',state=state)

@app.route('/about')
def about():
	global state
	
	return render_template("about.html",state=state)

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
