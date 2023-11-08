import random
from words import word_list
import subprocess
import platform


class Guess:
    """
    A class to represent a player's guess in a game.

    Attributes:
        user_guess (str): The player's guessed letter or word.

    Methods:
        __init__(user_guess): Initializes a new Guess object with the provided guess.
    """
    def __init__(self, user_guess):
        self.user_guess = user_guess


def get_guess():
    """
    Prompt the player for a letter or word guess and validate the input.
    Returns:
        str: A valid letter or word guessed by the player.
    """
    while True:
        guess = Guess(input("Please guess a letter or word: ").upper())
        if len(guess.user_guess) == 1 and guess.user_guess.isalpha():
            return guess.user_guess
        elif len(guess.user_guess) > 1 and guess.user_guess.isalpha():
            return guess.user_guess
        else:
            print("Invalid input. Please enter a single letter or a complete word.")


def get_difficulty():
    """
    Prompt the player to choose the game difficulty (easy/hard) and validate the input.
    Returns:
        str: The chosen difficulty level ('easy' or 'hard').
    """
    while True:
        difficulty = input("Choose difficulty (easy/hard): ").lower()
        if difficulty in ["easy", "hard"]:
            return difficulty
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")


def clear_screen():
    if platform.system() == "Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"], shell=True)
    else:  # Linux and Mac
        print("\033c", end="")


def get_word(difficulty):
    """
    Get a random word based on the selected game difficulty.

    Args:
        difficulty (str): The game difficulty level ('easy' or 'hard').

    Returns:
        str: A random word from the specified difficulty category.
    """
    if difficulty == "easy":
        word = random.choice(word_list["easy"])
    elif difficulty == "hard":
        word = random.choice(word_list["hard"])
    else:
        raise ValueError("Invalid difficulty level")
    return word.upper()


def play(word):
    """
    Play the Hangman game with the provided word.

    Args: word (str): The word to be guessed in the game.
    """
    clear_screen()  # Clear the screen before starting the game
    word_completion = "*" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    previous_guesses = []  # list of previous guesses

    print("""
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""".format(" "))    

    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = get_guess()
        clear_screen()

        if len(guess) == 1 and guess.isalpha():
            clear_screen()
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                previous_guesses.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indic = [i for i, letter in enumerate(word) if letter == guess]
                for index in indic:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "*" not in word_completion:
                    guessed = True
                previous_guesses.append(guess)

        elif len(guess) > 1 and guess.isalpha():
            if guess == word:
                guessed = True
                word_completion = word
            else:
                print(guess, "is not the word.")
                tries -= 1
                previous_guesses.append(guess)

        print(display_hangman(tries))
        print(word_completion)
        print("Previous guesses:", ", ".join(previous_guesses))
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    """
    Display the Hangman ASCII art based on the number of remaining tries.

    Args:
        tries (int): The number of incorrect guesses remaining.

    Returns:
        str: The ASCII art representation of the Hangman's current state.
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    """
    The main function to start and manage the game.
    """
    print("Welcome to Hangman!")

    while True:
        difficulty = get_difficulty()
        if difficulty in ["easy", "hard"]:
            break
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")

    while True:
        word = get_word(difficulty)
        play(word)

        while True:
            play_again = input("Play Again? (Y/N) ").upper()

            if play_again in ["Y", "N"]:
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

        if play_again != "Y":
            break


if __name__ == "__main__":
    main()
