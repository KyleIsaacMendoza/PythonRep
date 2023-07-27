# Create a board using 2D Array
# Logic on how to Display the Empty Board
# Logic on how to input X and 0
# Logic on how to Display the Board with the inputted information
# Logic on how to retain it
# Process on Winning or Winning Patterns
# Winning the Game


# Create board 
# This is a 2D board
board = [
    [1,2,3], #1,2,3
    [4,5,6], #4,5,6
    [7,8,9], #7,8,9
]



# Function to Introduction
def introduction():
    print("Welcome Players!")
    print("Just Press P to play and S to Stop")




# Function to Display Board
def displayBoard(): 
    print(f"-------------------")    
    print(f"|  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |")
    print(f"-------------------")       
    print(f"|  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |")
    print(f"-------------------") 
    print(f"|  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |")
    print(f"-------------------\n")

    



#? Function to Count all available position in the board 
#? Or remove picked numbers from the freePosition arr
def freeNumbers():
    freePosition = []
    print(freePosition)
    for i in range(0, len(board)):
        for x in range(0, len(board)):
            if board[i][x] == 'X' or board[i][x] == 'O':
                if board[i][x] in freePosition: #if position of board that is X or O is in freePosition Array
                    freePosition.remove(freePosition[board[i][x]])# remove the freePosition[position] from the freePosition Array
                continue
            else: 
                freePosition.append(board[i][x])    
    return freePosition




#? Function to SET board position into players answer 
# Example: player 1 X pick 1 as his move, then board[0][0] will be set to players Mark (X)
def executeAnswer(position, answer):
    match position:
        case 1:
            board[0][0] = answer
        case 2:
            board[0][1] = answer
        case 3: 
            board[0][2] = answer
        case 4:
            board[1][0] = answer
        case 5:
            board[1][1] = answer
        case 6:
            board[1][2] = answer
        case 7:
            board[2][0] = answer
        case 8:
            board[2][1] = answer
        case 9:
            board[2][2] = answer
        case _:
            print("You've Inputted Number that doesnt exist") # This is default




#? Function if there is a pattern on the BOARD
def checkWinner(player, answer):
    winner = 0
    if board[0][0] == answer and board[1][1] == answer and board[2][2] == answer:
        winner = player
    elif board[0][0] == answer and board[1][0] == answer and board[2][0] == answer:
        winner = player
    elif board[0][0] == answer and board[0][1] == answer and board[0][2] == answer:
        winner = player    
    elif board[0][1] == answer and board[1][1] == answer and board[2][1] == answer:
        winner = player   
    elif board[0][2] == answer and board[1][2] == answer and board[2][2] == answer:
        winner = player  
    elif board[1][0] == answer and board[1][1] == answer and board[1][2] == answer:
        winner = player   
    elif board[2][0] == answer and board[2][1] == answer and board[2][2] == answer:
        winner = player
    
    return winner #Return who wins player1 or player2





introduction() #introduction
displayBoard() #displayBoard
countBased = 0 #! count based Needed this will based how the answer mark will be



while True:
    answer = 'X' if countBased%2 == 0 else 'O' #? ternary operator in Python
    #player answer is based on countBased.
    player = 1 if answer == 'X' else 2 #? ternary
    
    
    print(f"Player {player} it's your Turn and your Mark is {answer}")
    blanks = freeNumbers() # blanks = arr that display freePosition 
    print(f"Here are the free numbers {blanks}\n") #Display the freePosition array
    position = int(input("Where do you want to place your Mark? ")) #position to where you want to place your mark [1-9] 2D array

    
    executeAnswer(position, answer) #set player answer into the position he picked he wanted to.
    displayBoard() #Display Board Updated
    
    
    
    # After moves or If blanks available move is only 4 remaining left, check if there is possible winner
    if len(blanks) <= 5:
        winner = checkWinner(player, answer)
        if winner == 1 or winner == 2:
            print(f"Player {winner} Wins")
            break #if there is a winner then end the game
        
    # if blanks (freePosition) equal zero meaning there is no available position left
    # print there is no winnner
    elif len(blanks) == 0:
        print("There is no winner")
        break
    
    
    countBased += 1 #Increment to change the player and the mark.


