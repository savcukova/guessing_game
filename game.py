import random
import os


def guessing_game():
    continue_game = "yes"
    while continue_game.lower() == "yes":
        os.system("clear")
        print("Welcome to the game 'Guess secret number'!")
        print("I have one number on my mind between 1 and 100. \n")
        level = choose_difficulty_level()
        secret_number = generate_secret_number()
        user_guess(secret_number, level)
        continue_game = want_continue()
    else:
        print("game over.")
    

def choose_difficulty_level():
    level = input("Choose level (write hard or easy): ").lower()
    if level not in ["hard", "easy"]:
        print("Invalid input, enter 'hard' or 'easy'.")
    
    if level == "easy":
        print("you choose easy level. You have 10 attemps to guess number. ")
    elif level == "hard":
        print("You choose  hard level. You have 5 attemps to guess number. ")
        
    return level
        
        
def generate_secret_number():
    secret_number = random.randint(1, 100)
    return secret_number
        
        
def user_guess(secret_number, level):
    attempts = 10 if level == "easy" else 5
        
    while attempts > 0:
        guess_input = input("Guess the secret number: ")
        
        if guess_input.isdigit():
            guess = int(guess_input)
            
            if 1 <= guess <= 100:
                if guess == secret_number:
                    print(f"Congratulations! You guessed the secret number {secret_number} correctly!")
                    return
                elif guess > secret_number:
                    print("Too high. Try again.")
                else:
                    print("Too low. Try again.")
            else:
                print("Choose a number in the range of 1 and 100.")
        else:
            print("Please enter a valid number.")
            
        attempts -= 1
        print(f"Attemps left: {attempts}")

    if attempts == 0:
        print("Sorry, you've run out of attemps. ")    
    
        
def want_continue():
    continue_game = input("Do you want to start new game? 'yes'/'no': ")
    return continue_game    
        
        
if __name__ == "__main__":
    guessing_game()