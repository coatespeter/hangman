import random
from words import word_list


def get_guess():
    while True:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            return guess
        elif len(guess) > 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single letter or a complete word.")


def get_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy/hard): ").lower()
        if difficulty in ["easy", "hard"]:
            return difficulty
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")


def get_word(difficulty):

    if difficulty == "easy":
        word = random.choice(word_list["easy"])
    elif difficulty == "hard":
        word = random.choice(word_list["hard"])
    else:
        raise ValueError("Invalid difficulty level")
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
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

        if len(guess) == 1 and guess.isalpha():
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
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
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
