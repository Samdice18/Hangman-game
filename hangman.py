import random as r


def select_random_word():
    with open("words.txt", "r") as word_file:
        words = word_file.readlines()
        random_word_index = r.randint(0,len(words))
        word = words[random_word_index].strip()

    return word


def mystery_word(selected_word):
    hidden_word = "_" * len(selected_word)

    return hidden_word


def hangman_graphics(number_of_guesses):

    Stick_figures = ["""
    +----+
    |    0
    |   \\|/
    |    |
    |   / \\
    |
    =========
    ""","""
    +----+
    |    0
    |   \\|/
    |    |
    |   / 
    |
    ========
    ""","""
    +----+
    |    0
    |   \\|/
    |    |
    |
    ========
    ""","""
    +----+
    |    0
    |   \\|/
    |
    |
    ========
    ""","""
    +----+
    |    0
    |   \\|
    |
    |
    ========
    ""","""
    +----+
    |    0
    |    |
    |
    |
    ========
    ""","""
    +----+
    |    0
    |    
    |
    |
    ========
    ""","""
    +----+
    |
    |
    |
    |
    ========
    """]

    print(Stick_figures[number_of_guesses])


def run_game(selected_word, mystery_word):
    number_of_guesses = 8
    not_guessed = True

    invalid_letters = []

    word_as_list = list(selected_word)

    mystery_word_list = list(mystery_word)

    guessed_letter = []

    print("""
 _                                                       _________
| |                                                     |/        |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __           |        (_)
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \          |        \\|/ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |         |         |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|         |        / \\
                    __/ |                               |
                   |___/                              __|__
    """)

    print("\nA random word has been selected and you have 8 turns to guess the word. \n")

    while not_guessed and number_of_guesses != 0:

        print(f"\nGuess the word: {mystery_word}")

        user_guess = input("Enter your guess: ")

        if len(user_guess) > 1:
            print("\nEnter only one letter and avoid numbers...\n")
            print("=========================================================================================\n")

        elif user_guess.isdigit() and len(user_guess) != 0:
            print("\nEnter only one letter and avoid numbers...\n")
            print("=========================================================================================\n")

            continue
        elif len(user_guess) == 1:
            if user_guess in selected_word and user_guess not in guessed_letter:
                for i in range((len(word_as_list)-1)):
                    if word_as_list[i] == user_guess:
                        mystery_word_list[i] = user_guess
                        mystery_word = "".join(mystery_word_list)
                        if select_random_word == mystery_word:
                            print("congratulations ...\n")
                            not_guessed = False
                    guessed_letter.append(user_guess)

            elif user_guess in invalid_letters or user_guess in guessed_letter:
                print("\nYou cannot guess the same later twice\n")
                print("\n=========================================================================================\n")
                continue
                
            elif user_guess not in selected_word:
                number_of_guesses -= 1
                print("\nIncorrect guess\n")
                hangman_graphics(number_of_guesses)
                invalid_letters.append(user_guess)
                print("\n=========================================================================================\n")
                
    if number_of_guesses == 0:
        print(f"The word was {selected_word}")
        print("Better luck next time...")


if __name__ == '__main__':
    selected_word = select_random_word()
    mystery_word = mystery_word(selected_word)
    run_game(selected_word, mystery_word)