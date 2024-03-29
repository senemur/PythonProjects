#Number Guessing Game Objectives:

# Include an ASCII art logo.
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Yay! You got it! The answer was {answer}.")


def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("You entered invalid type. Please type 'easy' or 'hard': ")


def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. ")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != answer:
            print("Guess again.")


game()
