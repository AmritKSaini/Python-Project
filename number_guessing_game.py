from random import randint
from art import logo

#TODO 1: choose a random number between 1 to 100.
#TODO 2: a function the set difficulty.
#TODO 3: let the user guess a number.
#TODO 4: check the guess against the actual answer.
#TODO 5: track the number of turns and reduce it by 1 if they get it wrong.
#TODO 6: repeat the guessing functionality if the guess is wrong.


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks the answer against guess, and returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too High.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    #function to set the difficulty of the game
    level = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!"
          "I'm thinking of a number between 1 to 100.")
    #Function to choose a randon number between 1 and 100
    answer = randint(1,100)
    print(f"Pssst. The correct answer is {answer}")

    turns = set_difficulty()

    #Repeat the guessing functionality if the guess is wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        #Let the user guess a number
        guess = int(input("Make a Guess: "))
        # Compare the number and reduce a turn if the guess is wrong.
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses. You Lose!")
            guess = answer
        elif guess != answer:
            print("Guess Again.")

game()