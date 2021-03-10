# Source: http://www.codeskulptor.org/#user48_gbs7AxDWFw_2.py
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

####################
# Global Variables
NUM_RANGE = 100
TARGET = 0
GUESSES = 0

####################
# Helper Functions

def new_game():
    """ Initializes a new game """
    global GUESSES, TARGET
    
    # Everytime you guess, you divide the interval in half. 
    # To gaurantee 1 number is left in the interval you have 
    # to get an interval of length 1. 
    # So, we solve:
    #		100/(2**n) = 1		(original)
    #		100        = 2**n 	(multiply both sides by 2**n)
    #		log2(100)  = n 	(take log base 2 of both sides)
    frac_guess = math.log(NUM_RANGE,2)
    
    # Convert to int because the number of guesses has to be an integer,
    # and math.ceil returns a float. Use math.ceil to account for values
    # of NUM_RANGE that are not powers of 2
    GUESSES = int(math.ceil(frac_guess))
    
    # Use randrange for [0,NUM_RANGE) interval
    TARGET = random.randrange(0,NUM_RANGE)
    
    # Display gameplay text
    print "New game. Range is from 0 to", NUM_RANGE
    guesses_left()
    print ""

def game_over(player_won):
    """ Displays game ending messages and transitions to a new game """
    if player_won:
        print "Correct!\n"
    else:
        print "You ran out of guesses. The number was", TARGET, "\n"
    new_game()
    
def guesses_left():
    """ Displays remaining number of guesses """
    print "Number of remaining guesses is", GUESSES

####################
# Event Handlers

def range100():
    """ Starts a new game with the range [0,100) """
    global NUM_RANGE
    NUM_RANGE = 100
    new_game()

def range1000():
    """ Starts a new game with the range [0,1000) """
    global NUM_RANGE
    NUM_RANGE = 1000
    new_game()
    
def input_guess(guess):
    """ Plays 'Guess the number' with the user, based on user input """
    print "Guess was", guess
    guess_num = int(guess)
    
    # updates guesses and reports it
    global GUESSES
    GUESSES -= 1
    guesses_left()
    
    # handles the guess itself
    if guess_num == TARGET:
        game_over(True)
    elif GUESSES <= 0:
        game_over(False)
    elif guess_num < TARGET:
        print "Higher!\n"
    elif TARGET < guess_num:
        print "Lower!\n"

####################
# GUI Frame
frame = simplegui.create_frame("Guess the number", 200, 200)

####################
# Connect Components
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

####################
# Start Frame
new_game()
frame.start()
