import random
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement
import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

try:
    from WordleAI import WordleAI as WordleAI
except ModuleNotFoundError:
    print("WordleAI.py is not found.")

from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses

class Wordle:
    def __init__(self, STYLES: dict[str, str], wordleAI:WordleAI): # wordleAI:WordleAI, secret_words:get_secret_words
        self.STYLES = STYLES
        self.wordleAI = wordleAI
        #self.wordleAI = wordleAI
    #    self.secret_word = get_secret_words()
        #target_word = random.choice(self.secret_word)
        self.guess_counter = 0
        self.secret_word = self.pick_secret()
    def pick_secret(self):
        random_secret = random.choice(list(get_secret_words()))
        return random_secret
    def get_guesses(self):
        guess = input("Enter guess: ")
        if len(guess) != 5:
            guess = input("Enter guess: ")
        return guess

    def play_game(self):
        print(STYLES["gray"] + "       ") #print top row
        stringz = STYLES["gray"] + " "
        while self.guess_counter <= 6:
            guess = self.get_guesses()
            for element in self.colored_guess(guess):
                stringz += element #add each letter with style block into stringz
            print(stringz)
            print(stringz + STYLES["gray"]+ " ")
            print(STYLES["gray"] + "       ")
            self.guess_counter+=1

    pass

    def colored_guess(self, guess: str) -> str:
        # returns each thing as a color blocked code of each letter to print
        colored_word = []

        print("guess", guess, "secret_word", self.secret_word)
        uncolored_guess = self.wordleAI.get_feedback(guess, self.secret_word)
        if colored_word:
            colored_word.append("\n")
        for i in range(len(uncolored_guess)):
            if uncolored_guess[i] == "-":
                colored_word.append(STYLES["black"] + guess[i].upper())
            elif uncolored_guess[i].islower(): # check if its lowercase
                colored_word.append(STYLES["yellow"] + guess[i].upper())
            else: # if upper
                colored_word.append(STYLES["green"] + guess[i].upper())
        return colored_word
if __name__ == "__main__":
    STYLES= {
            "yellow": Back.YELLOW+Style.BRIGHT,
            "green": Back.GREEN+Style.BRIGHT,
            "gray": Back.WHITE+Style.DIM,
            "black": Back.BLACK+Style.DIM
    }
    wordle = Wordle(STYLES, WordleAI(get_valid_wordle_guesses,get_valid_wordle_guesses))
    #print(str(wordle)+"\n")
    wordle.play_game()

    pass
