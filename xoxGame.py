gameBoard = [' ' for x in range(10)]

def ShowScreen():
    print(' ' + gameBoard[1] + ' ' + '|' + ' ' + gameBoard[2] + ' ' + '|' + ' ' + gameBoard[3])
    print("------------")
    print(' ' + gameBoard[4] + ' ' + '|' + ' ' + gameBoard[5] + ' ' + '|' + ' ' + gameBoard[6])
    print("------------")
    print(' ' + gameBoard[7] + ' ' + '|' + ' ' + gameBoard[8] + ' ' + '|' + ' ' + gameBoard[9])

def setMark(mark,pos):
    gameBoard[pos] = mark

def isEmptyArea(pos):
    return gameBoard[pos] == ' '

def FullArea():
    if gameBoard.count(' ') > 1:
        return False
    else:
        return True

def Winner(gameBoard, mark):
    return (gameBoard[1] == mark and gameBoard[2] == mark and gameBoard[3] == mark) or (gameBoard[4] == mark and gameBoard[5] == mark and gameBoard[6] == mark) or (gameBoard[7] == mark and gameBoard[8] == mark and gameBoard[9] == mark) or (gameBoard[1] == mark and gameBoard[4] == mark and gameBoard[7] == mark) or (gameBoard[2] == mark and gameBoard[5] == mark and gameBoard[8] == mark) or (gameBoard[3] == mark and gameBoard[6] == mark and gameBoard[9] == mark) or (gameBoard[1] == mark and gameBoard[5] == mark and gameBoard[9] == mark) or (gameBoard[3] == mark and gameBoard[5] == mark and gameBoard[7] == mark)

def PlayerMovement():
    pos = int(input("Type between of 1-9 position: "))
    if isEmptyArea(pos):
        setMark('X',pos)
        if Winner(gameBoard, 'X'):
            ShowScreen()
            print("Congratuations! You Won!")
            exit()
        ShowScreen()
    else:
        print("Invalid or full position, try again: ")
        PlayerMovement()

def BotMovement():
    import random
    available_positions = [pos for pos, mark in enumerate(gameBoard) if mark == ' ' and pos != 0]

    movement = 0

    for mark in ['O','X']:
        for i in available_positions:
            copy_board = gameBoard[:]
            copy_board[i] = mark
            if Winner(copy_board, mark):
                movement = i
                return movement
    corners = []

    for i in available_positions:
        for i in [1,3,7,9]:
            corners.append(i)

    if len(corners) > 0:
        movement = random.choice(corners)
        return movement

    if 5 in available_positions:
        movement = 5
        return movement

    inside = []

    for i in available_positions:
        for i in [2,4,6,8]:
            inside.append(i)

    if len(inside) > 0:
        movement = random.choice(inside)
        return movement


def game():
    print("XOX Game..")
    ShowScreen()

    while not FullArea():
        PlayerMovement()
        if FullArea():
            print("DRAW..")
            exit()

        print("__________________________")
        bot_movement = BotMovement()
        setMark('O', bot_movement)
        if Winner(gameBoard,'O'):
            ShowScreen()
            print("Bot WON! Try Again?")
            exit()


        ShowScreen()
        if FullArea():
            print("DRAW..")
            exit()
            print("__________________________")

print(gameBoard)
game()


#while not Winner('X'):
#    pos = int(input("Type between of 1-9 position: "))
#    setMark('X',pos)




