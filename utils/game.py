from typing import List
from random import choice

class Hangman:
    """Class defining a hangman game characterized by :
    - a list of all possible words to find
    - the amount of lives
    """
    lives: int = 5
    possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self) -> None:
        """
        Constructor of our class.
        """
        self.lives = Hangman.lives
        self.possible_words = Hangman.possible_words
        self.word_to_find = list(choice(self.possible_words))
        self.correctly_guessed_letters: List[str] = ["_" for char in range(len(self.word_to_find))]
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.game_running: bool = True

    def play(self) -> None:
        """
        Function : core of the game mechanics, asks for input, 
        checks for input validity, and checks if the user is right.
        """
        user_input = input("Type \"exit\" to quit or type a letter: ")
        if user_input == "exit":
            self.game_running = False
            return
        if user_input in self.wrongly_guessed_letters or user_input in self.correctly_guessed_letters:
            print("You already typed this letter")
            return
        elif len(user_input) != 1:
            print("Please type only one character")
            return
        elif (user_input.isupper()) or (user_input.isalpha() is False):
            print("It is not an lowercase letter")
            return
        if user_input in self.word_to_find:
            for count, letter in enumerate(self.word_to_find):
                # Remark : print(count) print(letter) : 
                # These 2 print output : 0 m 1 a 2 t 3 h 4 e 5 m 6 a 7 t 8 i 9 c 10 s because enumerate
                # outputs [(0,m),(1,a),(2,b)...(10,s)]
                if letter == user_input:
                    self.correctly_guessed_letters[count] = user_input
        else:
            print("There is no such letter in the mistery word")
            self.lives = self.lives - 1
            self.error_count +=1
            self.wrongly_guessed_letters.append(user_input)
        self.turn_count += 1

    def game_exit(self) -> None:
        """
        Function : exit the game by changing the value of a boolean variable
        """
        print("See you next time !")
        self.game_running = False
    
    def game_over(self) -> None:
        """
        Function : print
        """
        print("Game over...")

    def well_played(self) -> None:
        """
        Function : print
        """
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!.")
 
    def start_game(self) -> None:
        """
        Function start_game : main game loop, checks for defeat/victory conditions.
        """
        print("HANGMAN GAME LOADED\n")
        print(f"{self.correctly_guessed_letters}\n")
        while self.game_running == True:
            self.play()
            if self.lives == 0:
                self.game_over()
                break
            if self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break
            print(self.correctly_guessed_letters)
            print(f"Wrong trials : {self.wrongly_guessed_letters}")
            print(f"Lives left : {self.lives}")
            print(f"Mistakes : {self.error_count}")
            print(f"Turn count : {self.turn_count}")
        self.game_exit()