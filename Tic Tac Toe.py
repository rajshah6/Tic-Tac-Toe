def getIntInput(prompt = "Enter an integer: ", exceptStatement = "Invalid input. "):
    while True:
        try:
            var = int(input(prompt))
            return var

        except ValueError:
            print(exceptStatement, end = "")

# repeat game 
winsX = 0
winsO = 0
totalGames = 1

while True:
    # create board and index
    board = """
 1 | 2 | 3
-----------
 4 | 5 | 6  
-----------
 7 | 8 | 9  
"""
    index = {
        "1": " ",
        "2": " ",
        "3": " ",
        "4": " ",
        "5": " ",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " "
    }
    
    # print template board
    print("Square Interface:")
    print(board)

    player = "X"
    usedIdx = []
    playedIdx = {
        "X": [],
        "O": []
    }

    while True:
        # get inputs
        print(f"{player}'s Turn")

        squareIdx = getIntInput("What square would you like?: ")
        while squareIdx < 1 or squareIdx > 9:
            squareIdx = getIntInput("Invalid input. What square would you like?: ", "")
        
        # check if index is already used
        while squareIdx in usedIdx:
            squareIdx = getIntInput("Index already exists. What square would you like?: ", "")
        
        usedIdx.append(squareIdx)

        # update square input
        index[str(squareIdx)] = player
        tempBoard = board

        for idx in index:
            tempBoard = tempBoard.replace(idx, index[idx])
        print(tempBoard)

        # update played index
        playedIdx[player].append(squareIdx)

        # check for a win
        winConditions = [
        1 in playedIdx[player] and 2 in playedIdx[player] and 3 in playedIdx[player], 
        4 in playedIdx[player] and 5 in playedIdx[player] and 6 in playedIdx[player], 
        7 in playedIdx[player] and 8 in playedIdx[player] and 9 in playedIdx[player],
        1 in playedIdx[player] and 4 in playedIdx[player] and 7 in playedIdx[player], 
        2 in playedIdx[player] and 5 in playedIdx[player] and 8 in playedIdx[player], 
        3 in playedIdx[player] and 6 in playedIdx[player] and 9 in playedIdx[player],
        1 in playedIdx[player] and 5 in playedIdx[player] and 9 in playedIdx[player], 
        3 in playedIdx[player] and 5 in playedIdx[player] and 7 in playedIdx[player]
        ]

        if any(winConditions):
            print(f"Player with {player} wins!")
            if player == "X":
                winsX += 1 
            else:
                winsO += 1
            break

        # check for draw
        if sorted(playedIdx["X"] + playedIdx["O"]) == list(range(1, 10)):
            print("It's a draw!")
            break

        # change players
        if player == "X":
            player = "O"
        else:
            player = "X"
    
    playAgain = input("Would you like to play again? (y/n): ")
    if playAgain != "y":
        break

    totalGames += 1

print("\nTotal Games Played:", totalGames)
print("Player with X won", winsX, "time(s)")
print("Player with O won", winsO, "time(s)")