theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',  
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printBoard(board) :
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print("{0}|{1}|{2}".format(board['bot-L'], board['bot-M'], board['bot-R']))

def numToBoard(num) :
    li = ['top-L', 'top-M', 'top-R',
          'mid-L', 'mid-M', 'mid-R',  
          'bot-L', 'bot-M', 'bot-R']

    return li[num-1]

def CheckWinner(board) :
    li = [['top-L', 'top-M', 'top-R'],
          ['mid-L', 'mid-M', 'mid-R'],
          ['bot-L', 'bot-M', 'bot-R']]

    for i in range(3) :
        if(CheckSame(board[li[i][0]], board[li[i][1]], board[li[i][2]])) :
            return board[li[i][0]]
        if(CheckSame(board[li[0][i]], board[li[1][i]], board[li[2][i]])) :
            return board[li[0][i]]

    if(CheckSame(board[li[0][0]], board[li[1][1]], board[li[2][2]])) :
            return board[li[0][0]]
    if(CheckSame(board[li[0][2]], board[li[1][1]], board[li[2][0]])) :
            return board[li[0][2]]
    return ' '

def CheckSame(a, b, c):
    if a == b and b ==c :
        return True
    return False

turn = 'X'
for i in range(9) :
    printBoard(theBoard)
    print(f"Turn for {turn}. Move on which space?")
    
    move = input("Please enter 1-9: ")
    while True :
        if move.isnumeric() and int(move) >= 1 and int(move) <=9 :
            req = numToBoard(int(move))
            break
        else :
            print("Invalid!!! Please enter 1-9: ")
            move = input("Please enter 1-9: ")

    while True :
        if(theBoard[req] == ' '): 
            theBoard[req] = turn
            break
        else :
            print("Invalid!!! Please choose it again: ")
            move = input()
            req = numToBoard(int(move))
    
    if turn == 'X' :
        turn = 'O'
    else :
        turn = 'X'
    
    win = CheckWinner(theBoard)
    if(win == 'X') :
        print('X Win!!!!!!')
        break
    elif(win == 'O') :
        print('O Win!!!!!!')
        break


printBoard(theBoard)