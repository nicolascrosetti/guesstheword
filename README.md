# GUESS THE WORD
#### Video Demo:  <URL HERE>
#### Description:
Guess The Word is a word game inspired by Wordle. The goal of the game is to find the word of the day, which always has 5 letter. These are the rules of the game:
- There are 5 rounds
- Each guess must be a valid 5 letter word
- The color of the letters will change to show how close your guess was to the word
    - If the letter is white it means the letter is not in the word in any spot
    - If the letter is yellow it means the letter is in the word but not in that spot
    - If the letter is green it means the letter is in the word and in the correct spot

##### Files:

- project.py: The main file, contains all the game's functions and logic
- test_project.py: Contains all the tests to verify the functions in project.py work properly
- requirements.txt: Contains a list of all the pip installable libraries the project uses (in thsi case Colorama)
- words.csv: Contains a list of all the possible words of the day, which will be used in project.py to select a random word of the day
- valid_words: Contains a list of all english 5 letter words to validate the player's guess is a valid word
- README.md: This file; contains the project's desccription

##### project.py:

This is the main file where all the game's functions and logic reside. Here are the functions and their descriptions:

###### main:
The main function is divided in four parts:
- Todays word: calls the get_todays_word function to get the word of the day and stores it in todays_word variable
- Menu: calls the menu function to showcase the game's menu
- Play Five Rounds: it uses a for loop in which it calls the play_round function for 5 times to play the five rounds
- Player Lost: If after 5 rounds the game hasn't ended it means that the player has lost, so we show the player that they lost with a message and we call the handle_restart function to ask them if they want to play again or they want to exit the game

###### get_todays_word:
This function gets all the words in the file "words.csv" and stores them into the list "words" and then selects and return a random word from that list using the funcion choice from the library random

###### get_valid_word:
This function gets all the words in the file "valid_words.txt" and stores into the list valid_words and return that list

###### check_guess:
This function takes three arguments: user_guess, current_guess and todays_word. First it checks if the current guess is the correct answer (the word of the day), in that case the player has won so we tell them that by showing and message and we call the handle_restart function to ask them if they want to play again or they want to exit the game. If the current guess is not the correct word then it check if any of the letters of the guess are in the word of the day, if that's the case we store the correct colors to show that in the current_guess dictionary using Colorama's Fore function (green if the letter is in the correct spot or yellow if it's in the word but on the wrong spot)

###### menu:
This function prints the menu so the user can choose a command to either start the game, read the rules or exit the program. There are three commands:
- start
- rules
- exit

###### play_round:
This function takes two arguments: round_number and todays_word. First it creates the current_guess dictionarty where the information abour the current guess will be stored. Then it calls the get_user_guess function to get the player's guess. After that it calls the check_guess function to see if the user has won or get an updated version of the current_guess dictionary which will be stored in the updated_guess variable. And finally it prints the letters the user guess with the correct colors according to the check_guess function.

###### get_user_guess:
This function starts calling the get_valid_words() function and stores the list it gets in valid_words. Then it prompts the player to input a guess and it checks if the guess has exactly 5 letters and is one of the valid words that we got from the get_valid_words function. If the guess is invalid it will re-prompt the player until they input a valid word and when that happens it returns the guess.

###### handle_restart:
This function asks the player if they would like to play again. The player has to type either "yes", "y", "no" or "n". if they type yes, the function will call the main function and then game will start again if they type "no" then we will show a farewall message and exit the game.

##### test_proyect.py:
This file contains all the tests to verify that the functions in project.py work properly. Here are the functions and their descriptions:

###### test_get_todays_word:
This function tests the get_todays_word function in project.py. It makes sure that the function returns a 5 letter word (by using the len() function)

###### test_get_valid_words:
This functiont tests the get_valid_word function in project.py. It makes sure that the function returns a list with 12920 words (by using the len() function)

###### test_check_guess:
This function tests the check_guess function in project.py. It makes sure that by inputting a guess, a current_guess dictionary with the guess information and the word of the day we get the correct letters from the guess, the correct colors to show if the letter is or isn't part of the word and if it's in the correct spot or not (it checks if we get the correct current_guess object that will be later stored in updates_guess and printed on the screen inside the play_round function)



