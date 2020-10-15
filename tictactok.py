#--This is a 2 player game of tic tac toe
# by Gerardo Ocon

playerOne = True
gameContinues = True
wrongAnswer = True
tie = False
firstPlayer = ''
secondPlayer = ''
row = ''
column = ''

board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

# Welcome to the game
print('This is a new game of TIC TAC TOE!\n')

#Make sure player pick their corresponde
#If the user picks something that they are not to pick
#then it will let them know and they have to pick something else
while(wrongAnswer):
    firstPlayer = input('First player, Do you want to be X or O?\n')
    firstPlayer = firstPlayer.upper()
    if firstPlayer == 'X' or firstPlayer == 'O':
        print('Thank you!')
        wrongAnswer = False
    elif firstPlayer.isdigit() == False:
        print('That is not a number that I asked for.')
    else:
        print("That's not what I asked dummy. Pick again.")

#This is to pick the second player
if firstPlayer == 'X':
    secondPlayer = 'O'
else:
    secondPlayer = 'X'

#This is where the magic happens
#Puts the input number on the array
def magic():

    #This is a global variable to be able to change players
    global playerOne

    #Change the parameters to int instead of str
    theRow = int(row)
    theColumn = int(column)

    #If statement will determine if player 1 or 2 are playing
    if playerOne == True:
        #Changing the value of playerOne to False
        #Subtracting 1 from the column and row will make it so it doesnt over flow
        playerOne = False
        board[theRow - 1][theColumn - 1] = firstPlayer
    else:
        #Changing to value of playerOne to True
        #Subtracting 1 from the column and row will make it so it doesnt over flow
        playerOne = True
        board[theRow - 1][theColumn - 1] = secondPlayer


#To get the numbers fom the user
#For now it will be different questions
#Rows first, then columns
def themNumbers():

    global row
    global column
    greaterThan = True
    checking = False

    #Prompt the user again if the number is greater than 3
    while greaterThan == True:
        row = input('Enter a row position: ')
        column = input('Enter a column position: ')
        row = int(row)
        column = int(column)

        if row > 3 or column > 3:
            print('That is impossible, try again.')
        elif row == 0 or column == 0:
            print('Come on try again.')
        elif checkMove(row, column) == False:
            print('This move is already taken. Pick another one.')
        elif checkMove(row, column) == True:
            greaterThan = False
        else:
            greaterThan = False

#Checking if the input numbers are good for the board
def checkMove(row, column):
    if board[row - 1][column - 1] == ' ':
        return True
    else:
        return False


#Checking if there is a win in the game
def isThereWin():

    global tie

    #The making of new columns to see if the player has won
    column1 = []
    column2 = []
    column3 = []

    for x in range(3):
        column1.append(board[x][0])
        column2.append(board[x][1])
        column3.append(board[x][2])

    #Making strings of the diagnolly wins
    bottonToTop = board[2][0] + board[1][1] + board[0][2]
    topToBotton = board[0][0] + board[1][1] + board[2][2]

    #Checking all the different cases were there can be a win
    #If there is a win on rows
    #If any of this is true then the game will end
    if ''.join(board[0]) == 'XXX' or ''.join(board[0]) == 'OOO' :
        return True
    elif ''.join(board[1]) == 'XXX' or ''.join(board[1]) == 'OOO' :
        return True
    elif ''.join(board[2]) == 'XXX' or ''.join(board[2]) == 'OOO' :
        return True
    #If there is a win on columns
    elif ''.join(column1) == 'XXX' or ''.join(column1) == 'OOO' :
        return True
    elif ''.join(column2) == 'XXX' or ''.join(column2) == 'OOO' :
        return True
    elif ''.join(column3) == 'XXX' or ''.join(column3) == 'OOO' :
        return True
    #If there is a win diagnolly
    elif bottonToTop == 'XXX' or bottonToTop == 'OOO':
        return True
    elif topToBotton == 'XXX' or topToBotton == 'OOO':
        return True
    #This will determine if the board is full and game needs to be over
    elif ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        tie = True
        return True
    else:
        return False

#Display the game
def display():
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('-----------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('-----------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]}')

#Displays who is the winner of the game
def whoIsTheWinner():
    if tie == True:
        print('Is it a tie!')
        print('We are all winners or losers.')
    elif playerOne == False:
        print('Player One is the Winner!!')
        print('We knew you were the one and only!')
    else:
        print('Player Two is the Winner!!')
        print('The second pick always the best pick!')

#while game is not over
#It will continue the game
while (gameContinues):
    themNumbers()
    magic()
    display()
    if isThereWin() == True:
        whoIsTheWinner()
        gameContinues = False
