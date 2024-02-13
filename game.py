def guessing_game():
    print("Welcome to the game 'Guess secret number'!")
    print("I have one number on my mind between 1 and 100. \n")
    
    choose_hard_level()
    

def choose_hard_level():
    level = input("Choose level (write hard or easy): ").lower()
    
    if not level.isalpha:
        print("Invalid input, enter a word 'hard' or 'easy'.")
    else:
        pass
    
    if level == "easy":
        print("you choose easy level. ")
        #dale zde bude funkce pro easy level 
    elif level == "hard":
        print("You choose  hard level. ")
        





if __name__ == "__main__":
    guessing_game()