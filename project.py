import sys,csv
from random import choice as random_choice
from colorama import Fore


def main():
    #todays word
    todays_word = get_todays_word()

    #menu
    menu()

    #play five rounds
    for i in range(1,6):
        play_round(i, todays_word)
    
    #player lost
    print(Fore.RED + "You lost!, today's word was " + Fore.GREEN + todays_word)
    handle_restart()


def get_todays_word():
    words = []
    try:
        with open("words.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                words.append(row[0])
    except:
        sys.exit("Couldn't open words.csv file")

    return random_choice(words).upper()

def get_valid_words():
    valid_words = []

    with open("valid_words.txt") as file:
        for line in file:
            valid_words.append(line)
    
    valid_words = valid_words[0].split(" ")
    return valid_words

def check_guess(user_guess, current_guess, todays_word):
    if(user_guess == todays_word):
        has_won = True
        print("\n")
        print(Fore.GREEN+"Correct, well done!")
        handle_restart()
        
    else:
        for i,user_word in enumerate(user_guess):
            current_guess["guess"][i] = user_word
            if user_word in todays_word:
                positions = [i for i, word in enumerate(todays_word) if word == user_word]
                if i in positions:
                    for pos in positions:
                        if i == pos:
                            current_guess["colors"][i] = Fore.GREEN
                else:
                    current_guess["colors"][i] = Fore.YELLOW
        return current_guess

def menu():
    print(f"{Fore.BLUE}Welcome to Guess the Word!{Fore.WHITE}")
    while True:
        print(f"To begin the game, type '{Fore.BLUE}start{Fore.WHITE}'. If you'd like to learn how to play, type '{Fore.BLUE}rules{Fore.WHITE}'. To exit the game, type '{Fore.BLUE}exit{Fore.WHITE}'")
        menu_command = input(">: ").lower()
        if menu_command == "start" or menu_command == "rules" or menu_command == "exit":
            break
        else:
            print(f"{Fore.RED}Invalid command!{Fore.WHITE}")
    if(menu_command == "exit"):
        sys.exit()
    elif(menu_command == "rules"):
        print(f"{Fore.BLUE}How to Play: {Fore.WHITE}")
        print("-There are 5 rounds")
        print("-Each guess must be a valid 5 letter word")
        print("-The color of the letters will change to show how close your guess was to the word")
        print(" .If the letter is white it means the letter is not in the word in any spot")
        print(f" .If the letter is {Fore.YELLOW}yellow{Fore.WHITE} it means the letter is in the word but not in that spot")
        print(f" .If the letter is {Fore.GREEN}green{Fore.WHITE} it means the letter is in the word and in the correct spot")
        print("\n")
    else:
        print("\n")

def play_round(round_number, todays_word):
    current_guess = {
        "guess": ["_","_","_","_","_"],
        "colors": [Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE]
    }

    #get users guess
    user_guess = get_user_guess(round_number)
    updated_guess = check_guess(user_guess, current_guess, todays_word)
    #print rounds guess results
    for i,letter in enumerate(updated_guess["guess"]):
        print(current_guess["colors"][i] + letter, end="  ")
    print(Fore.WHITE + "\n")

def get_user_guess(round_number):
    valid_words = get_valid_words()
    while True:
        user_guess = input(f"{Fore.WHITE}Round {round_number} - Guess: ").upper()
        if len(user_guess) != 5:
            print(Fore.RED + "Your guess has to have 5 letters!")
        elif user_guess in valid_words:
            return user_guess
        else:
            print(Fore.RED + "Invalid word!")


def handle_restart():
    print("\n")
    while True:
        restart = input(Fore.WHITE + "Would you like to play again? (yes/no): ")
        if(restart == "yes" or restart == "y" or restart == "n" or restart == "no"):
            break
    if restart == "yes" or restart == "y":
        print("\n")
        main()
    else:
        sys.exit(f"{Fore.BLUE}Thank you for playing, have a nice day!{Fore.WHITE}")

if __name__ == "__main__":
    main()