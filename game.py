import random


def guessing_game():
    print("Welcome to the game 'Guess secret number'!")
    print("I have one number on my mind between 1 and 100. \n")
    
    continue_game == "yes"
    while continue_game.lower() == "yes":
        level = choose_difficulty_level()
        secret_number = generate_secret_number()
        user_guess(secret_number, level)
        continue_game = want_continue()
    else:
        print("game over.")
    

def choose_difficulty_level():
    level = input("Choose level (write hard or easy): ").lower()
    
    if not level.isalpha:
        print("Invalid input, enter a word 'hard' or 'easy'.")
    else:
        pass
    
    if level == "easy":
        print("you choose easy level. You have 10 attemps to guess number. ")
        #dale zde bude funkce pro easy level 
    elif level == "hard":
        print("You choose  hard level. You have 5 attemps to guess number. ")
        
    return level
        
        
def generate_secret_number():
    secret_number = random.randint(1, 100)
    return secret_number
        
        
def user_guess(secret_number, level):
    if level == "easy":
        attemps = 10
    elif level == "hard":
        attemps = 5
        
    while attemps > 0:
        guess = int(input("Guess the secret number: "))
        
        if guess == secret_number:
            print(f"Congratulation, you guess the secret number {secret_number} correct! ")
            break
        elif guess > secret_number:
            print("Too high number. Try again. ")
        else:
            print("Too low. Try again. ")
            
        attemps -= 1
        print(f"Attemps left: {attemps}")

    if attemps == 0:
        print("Sorry, you've run out of attemps. ")    
    
    
def want_continue():
    continue_game = input("Do you want to start new game? 'yes'/'no': ")
    return continue_game    
        
        
if __name__ == "__main__":
    guessing_game()