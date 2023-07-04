# This is my First Project.
# This program will generate random number from 0-10 and the user must guess it right


# import random to use random.randint(start, end)

import random


# variables to store random number and user input 
# check if the user guess is correct
# optional ( score if the user is correct)
# optional ( if the user win or the score is 5 )


# Declaration 
choice  = 'Y' # default choice is Yes to run the loop atleast 1 time.



# function to generate the random number
def generate_number():
    return random.randint(0,9)



# function to welcome the user and it will recieve user's name
def welcome_message(name):
    print(f"\nWelcome {name} Do you want to play a Game?: ")
    print("To play enter 'Y' and enter any key to stop")
    return (input(f"Hello, {name}. 'Y' -> Yes or Any -> No:  ")).capitalize()


# introduction of the game if the user wants to play.
def explanation_of_game(name):
    print(f"\n\nI will explain the game now to you {name}")
    print("\tTo Play the Game\n")
    print("You need to guess the random number from 0 to 9.")
    print("This will Test how lucky you are!")
    print(f"Let's Start {name}!")
  
  
  
# check if the user win or not. and display message
def checkWin(score, name):
    if(score > 5):
        print(f"\nYou have a total score of {score} out of 10.")
        print(f"Congratulations {name}! You win!")
    else:
        print(f"\nYou have a total score of {score} out of 10.")
        print(f"It's Ok {name}, Better luck next time!")
    
    
    
    
# function to ask the name of the user
def askName():
    print("\nHello! I am Python, What's your Name?")
    return input("> ")






# choice will receive if the user input Y or dont want to play the game.
# Loop to ask the user if he/she wanted to play the guessing game
while choice == "Y":
    
    # declare users_name
    # to save the users name that you ask.
    users_name = askName()
    
    # Check if the user wants to play AGAIN
    choice = welcome_message(users_name)
    
    
    # Function to Explain the game 
    explanation_of_game(users_name)
    
    # Default value of Count is 1 for better reading.
    count = 1
    user_score = 0
    for count in range(1,11): 
        # range of 10 1,2,-> 10
        # inside the random_number variable is the random number we receive in the function GENERATE_NUMBER()
        # this random number will change every iteration.
        random_number = generate_number()
        
        print(f"\n{users_name} Guess the ??? number!")
        answer = int(input(f"{count}. Guess: ")) # convert the input into int to have them compared later on.
        
        # if correct score + 1
        if(answer==random_number): 
            print(f"Correct! The random number is {random_number}")
            user_score+=1
        # if the score is wrong, then score will remain.
        elif(answer!=random_number): 
            print(f"I'm sorry {users_name}. The correct answer is {random_number}.")
        # just in case
        else:
            print(f"Something happen! Error...")
    
    # check
    checkWin(user_score, users_name)
    
    
            
    