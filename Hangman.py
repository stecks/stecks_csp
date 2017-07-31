class Hangman():
#Thanks to Darvyn for this code!
#Thanks to Jessica for helping me debug the code.
#We start with a function that descibes the game and instructions.

#In []: is an example of an absolute value function
#Def X(): defines a function 
#Print (): is a function that prints whatever is in the single quotes
#if is a boolean function that only returns a true expression
#else is a boolean function that only returns a false expression
#Quotation marks 'letter' or "spaces" are strings of data
#Parentheses ( e1, e2, e3 ) are tuples
#tuples are values in parentheses (2,4,8) that cannot be edited. a = (2,4,8) a is now the tuple.
#lists are values that occur within square brackets and can be edited. 
#Curly braces {key1 : value1, key2 : value2} provides a dictionary of items
#rawinput() provides a method for user input.
#import X - import must occur at the top/first line of a program
#random functions: 
#random.choice (values) - choose from a list 
#random.randint(5,8) - choose int from 5 - 8
#random.uniform(5,8) - choose float between 5 & 8


	def __init__(self):
#The user is presented with a decision point to either play or leave the game.
		print "Welcome to 'Hangman.' Hangman is a game that starts with a secret word that must be revealed before you run out of options and die?"

		print "(1)Yes, ready the gallows\n(2)No, get me outta here!"

		user_choice_1 = raw_input("->")

#After starting the game the user guesses a letter, enter and the program returns either a successful attempt or a move closer to the gallows.		

		if user_choice_1 == '1':

			print "First the executioner must test the gallows by dropping some sand bags"

			self.start_game()

		elif user_choice_1 == '2':

			print "Good bye..."

		else:

			print "I'm sorry, I'm hard of hearing, could you repeat that?"

			self.__init__()



	def start_game(self):

		print "The gallows passed the test and is ready."

		print "Now the prisoner is brought out."

		print "Officials, media and the public have gathered."

		print "The judge asks if the prisoner has any last words"

		print "The prisoner is hooded and the noose is placed around his neck"

		print "The Judge reads outloud the final decision, by the powers vested in me by the state of PLTW let the exection begin."

		print "The prisoner's is given last rights"

		print "Whether or not the prisoner dies or lives is in your hands so choose wisely!"

		self.core_game()

#With each successive wrong answer the gallows image gains a symbol until all are used and the user and prisoner lose.
#With each successively correct answer the user and prisoner move toward winning a stay of execution. 

	def core_game(self):

		guesses = 0

		letters_used = ""

		the_word = "scott"

		progress = ["?", "?", "?", "?", "?"]

		

		while (guesses < 6) and ("?" in progress):

			guess = raw_input("Guess a letter ->")



			if guess in the_word and not (guess in letters_used):

				print "Your guess was RIGHT, earning the prisoner a temporary stay!"

				letters_used += "," + guess

				self.hangman_graphic(guesses)

				print "Progress: " + self.progress_updater(guess, the_word, progress)

				print "Letter used: " + letters_used

			elif guess not in the_word and not(guess in letters_used):

				guesses += 1

				print "Your guess was WRONG!" 

				print "The crowd is growing more excited"

				print "and demand justice?"

				letters_used += "," + guess

				self.hangman_graphic(guesses)

				print "Progress: " + "".join(progress)

				print "Letter used: " + letters_used

			else:

				print "That's the wrong letter, the grim reaper awaits?"

			
			print "Try again and pay attention!"
                
                if "?" not in progress:
                    print "You WON, the prisoner lives!"
                else:
                    print "You LOSE, you have carried out the first execution of this week and its only Monday!"


#Below are the successive fuctions displayed as wrong answers are given.


	def hangman_graphic(self, guesses):

		if guesses == 0:

			print "________      "

			print "|      |      "

			print "|             "

			print "|             "

			print "|             "

			print "|             "

		elif guesses == 1:

			print "________      "

			print "|      |      "

			print "|      0      "

			print "|             "

			print "|             "

			print "|             "

		elif guesses == 2:

			print "________      "

			print "|      |      "

			print "|      0      "

			print "|     /       "

			print "|             "

			print "|             "

		elif guesses == 3:

			print "________      "

			print "|      |      "

			print "|      0      "

			print "|     /|      "

			print "|             "

			print "|             "

		elif guesses == 4:

			print "________      "

			print "|      |      "

			print "|      0      "

			print "|     /|\     "

			print "|             "

			print "|             "

		elif guesses == 5:

			print "________      "

			print "|      |      "

			print "|      0      "

			print "|     /|\     "

			print "|     /       "

			print "|             "

		else:

			print "________      "

			print "|      |      "

			print "|      0      "

			print "|     /|\     "

			print "|     / \     "

			print "|             "

			print "The noose tightens around his neck, and you feel the"

			print "crowd leans in. Snap and thud as the sentence is carried out"

			print "You have carried out the first execution of this week and its only Monday, GAME OVER!"

			self.__init__()



	def progress_updater(self, guess, the_word, progress):

		i = 0

		while i < len(the_word):

			if guess == the_word[i]:

				progress[i] = guess

				i += 1

			else:

				i += 1



		return "".join(progress)



game = Hangman()