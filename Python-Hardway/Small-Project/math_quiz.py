# I will create a Math quiz Score to win is 10 and to you will have a negative score
# Create a function on what operation you will have a test in
# Display the problem
# User will answer
# Function to Check
# Do user want to play again



# We will use random.randint() for our numbers
import random


# Operations function 
def addition(x,y):
    return x + y


def subtraction(x,y):
    return x - y


def multiplication(x,y):
    return x * y


def division(x,y):
    return x / y


# Function to Ask a Name
def askName():
    print("\nHello! Welcome to Math Quiz Game.")
    print("\nWhat is your Name? ")
    return input("> ").capitalize()


# Function to explain the Game
def gameIntro(player):
    print(f"\nSo, {player}. This is how we play this game.")
    print("* You need to choose on what Operation you want to take on QUIZ")
    print("* Is it, Addition, Subtraction, Multiplication, or Division ?")
    print("*\n\t Operation (Press The Number)")
    print("\t\t1 - Addition")
    print("\t\t2 - Sutraction")
    print("\t\t3 - Multiplication")
    print("\t\t4 - Division")


# Function choice of Operation
def userChoice(player):
    print(f"\nSo, {player}. What Operation you will choose? ")
    return int(input("> "))


# Function to check if the answer is correct ( You can have a function argument )
def checkAnswer(operation_func, x, y, userAnswer, gameScore):
    correct_answer = operation_func(x,y)
    
    if(correct_answer==userAnswer):
        print(f"\nCorrect!")
        gameScore+=1 # +1 to score
        return gameScore
    else:
        gameScore-=1 # -1 to score
        print(f"Wrong. The correct answer is {correct_answer}")
        return gameScore

# to Check the Score
def checkScore(score,name):
    if(score == 5):
        print(f"{name} You win! 5 Consecutive correct answers!")
    return  print(f"Your Current Score is: {score}")



# Loop for Program
while True:
    
    user_name = askName() # declare user_name and calling a function
    count = 1; # for counting the question
    gameScore = 0 # -0 for default gameScore
    gameIntro(user_name) # instructions about the game
    
    # store choice
    choice = userChoice(user_name)
    
    #  Addition
    if(choice == 1):
        print(f"\n{user_name} You've picked Addition.")
        
        # Loop for Questions
        while gameScore != 5:
            x = float(random.randint(0,100))
            y = float(random.randint(0,100))
            print(f"\n{count}. Solve {x} + {y} ")
            users_answer = float(input("> "))
            gameScore = checkAnswer(addition, x, y, users_answer, gameScore) # set return value as value of gameScore
            checkScore(gameScore, user_name)
            
    # Subtraction
    elif(choice == 2):
        print(f"\n{user_name} You've picked Subtraction.")
        
        #Loop for Question
        while gameScore != 5:
            x = float(random.randint(0,100))
            y = float(random.randint(0,100))
            print(f"\n{count}. Solve {x} - {y} ")
            users_answer = float(input("> "))
            gameScore = checkAnswer(subtraction, x, y, users_answer, gameScore) # set return value as value of gameScore
            checkScore(gameScore, user_name)
    
    # Multiplication
    elif(choice == 3):
        print(f"\n{user_name} You've picked Multiplication.")
        
        #Loop for Question
        while gameScore != 5:
            x = float(random.randint(0,100))
            y = float(random.randint(0,100))
            print(f"\n{count}. Solve {x} x {y} ")
            users_answer = float(input("> "))
            gameScore = checkAnswer(multiplication, x, y, users_answer, gameScore) # set return value as value of gameScore
            checkScore(gameScore, user_name)
    
    # Division
    elif(choice == 4):
        print(f"\n{user_name} You've picked Multiplication.")
        
        #Loop for Question
        while gameScore != 5:
            x = float(random.randint(1,100))
            y = float(random.randint(1,10))
            print(f"\n{count}. Solve {x} / {y} ")
            users_answer = float(input("> "))
            gameScore = checkAnswer(division, x, y, users_answer, gameScore) # set return value as value of gameScore
            checkScore(gameScore, user_name)
            
    else:
        print(f"{user_name}, Your choice {choice} is invalid. Please Try Again.")
        break #break the loop if the input of operation is invalid ( out of 1 - 4 )
    