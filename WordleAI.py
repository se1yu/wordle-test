import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses

class WordleAI:
    def __init__(self, all_valid_words: list[str], valid_wordle_answers: list[str]):
        self.valid_guesses = all_valid_words
        self.possible_answers = valid_wordle_answers
        # Add additional data attributes as needed
        pass

    def get_feedback(self, guess: str, secret_word: str) -> str:
        '''Generates a feedback string based on comparing a 5-letter guess with the secret word.
            The feedback string uses the following schema:
                - Correct letter, correct spot: uppercase letter ('A'-'Z')
                - Correct letter, wrong spot: lowercase letter ('a'-'z')
                - Letter not in the word: '-'

            Args:
                guess (str): The guessed word
                secret_word (str): The secret word

            Returns:
                str: Feedback string, based on comparing guess with the secret word

            Examples
            >>> AI = WordleAI(get_valid_wordle_guesses(), get_secret_words())
            >>> AI.get_feedback("lever", "EATEN") == "-e-E-"
            True
            >>> AI.get_feedback("LEVER", "LOWER") == "L--ER"
            True
            >>> AI.get_feedback("MOMMY", "MADAM") == "M-m--"
            True
            >>> AI.get_feedback("ARGUE", "MOTTO") == "-----"
            True
        '''
        feedback_string = ["-","-","-","-","-"]
        letter_counter = {}
        guess = guess.upper()
        secret_word = secret_word.upper()

        for letter in secret_word:
            if letter in letter_counter.keys():
                letter_counter[letter.upper()] += 1
            else:
                letter_counter[letter.upper()] = 1

        for i in range(len(guess)): #iterate thru all the first ones first because it takes priority for which is correct
            if guess[i] == secret_word[i]:
                feedback_string[i] = guess[i].upper()
                letter_counter[guess[i]] -= 1

        for i in range(len(guess)):
            if guess[i] in secret_word and letter_counter[guess[i]] > 0: # also include a counter and create a second for loop
                if feedback_string[i] == "-":
                    letter_counter[guess[i]] -= 1
                    feedback_string[i] = guess[i].lower()
        return "".join(feedback_string)

        pass

    def guess(self, guesses: list[str], feedback: list[str]) -> str:
        '''Analyzes feedback from previous guesses/feedback (if any) to make a new guess

        Args:
            guesses (list): A list of string guesses, which could be empty
            feedback (list): A list of feedback strings, which could be empty

        Returns:
            str: a valid guess that is exactly 5 uppercase letters
        '''
        

        pass

if __name__ == "__main__":
    AI = WordleAI(get_valid_wordle_guesses(), get_secret_words())
    print(AI.get_feedback("LEVER", "LOWER")) #"L--ER"
    guesses = ["CRANE", "CATER"]
    feedback = ["cra-e", "cater"]
    print(AI.guess(guesses, feedback)) #REACT
