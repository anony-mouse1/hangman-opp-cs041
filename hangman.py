import re

# start of hangman python project
print("Start of hangman python project")


# two objects---
# set of hashed strings that player will see at the start of the game
# the actual string itself

# two attributes: have an empty word bank. if the letter that player chooses has been used, then simply check the
# word bank to see if that letter already exists in the word bank, and if it does, ask player for another input. if
# it doesn't exist yet in the word bank, add the letter to the word bank and check if it's in the string.

class Game:
    def __init__(self):
        while True:
            self.word = input("Insert word you want player to guess: ")
            if not self.word.islower():
                print("Please put your word in lower-case!")
            else:
                print("Hiding word...")
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                break
        self.word = list(self.word)
        self.word_bank = []
        # add a bunch of print() so in console player will not be able to see your word
        self.tries = 7
        self.user_guess = []

    def start_empty_guess(self):
        self.user_guess = ['_' if i != ' ' else i for i in self.word]
        print(f"Player, you have {len(self.user_guess)} letters (inclusive of whitespace) to figure out.")
        print(f"You start off with:  {' '.join(self.user_guess)}")
        # give amount of letters in the string, include whitespace

    def make_guess(self):
        # if self.tries == 0:
        #   print("No more tries left! Sorry! ")
        #  break
        # add this statement when combining all the code together.
        while True:
            make_guess = input("Make a guess! It can be a number or a letter!")
            # print(type(make_guess)) make_guess will always be a string, no bother in converting it into a string
            # when it already is
            if (len(make_guess) != 1) or (make_guess in self.word_bank):
                print("Sorry, you have either entered too many characters or you have entered a letter/number that "
                      "has already been said!")
                # print the type of make_guess to make sure that it is a string first
                # continue is not needed here, since it will keep running this unless given a valid response
            else:
                # we are happy with the value given
                if make_guess in self.word:
                    for n, i in enumerate(self.word):
                        if i == make_guess:
                            self.user_guess[n] = make_guess
                    # if the guess is not the letter in self.word, then put the current user_guess instead. if the
                    # guess is the letter, then replace it will self.guess
                    print(
                        f"Great job! Your guess was part of the word(s)! Your updated guess: {(' '.join(self.user_guess))}")
                else:
                    print("Letter/number was not in word!")
                    self.tries -= 1
                    print(f"Your updated tries are...{self.tries}")
                self.word_bank.append(make_guess)
                break

    def word_completed(self):
        return self.user_guess == self.word
        # if returns True, then the word is completed
        # if it returns False, then the word is not completed yet

        # run this before running make_guess program

    def check_tries(self):
        return self.tries


while True:
    game = Game()
    game.start_empty_guess()
    while True:  # if the tries are 0 or the word is not completed:
        if game.check_tries() == 0:
            print("No more tries left! Sorry!")
            break
        if game.word_completed():
            print(f"Congrats, you guessed the word! Your word was completed! The word was: {''.join(game.word)}")
            # print(game.word)
            # print(game.user_guess) (same type of string)
            break
        else:
            game.make_guess()
# class Word_Bank():


# if the element count the first list is equal to the '' count  -1, then the string works!
