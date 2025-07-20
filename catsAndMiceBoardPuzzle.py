def findOccupiedSquares(coord):
    occupiedSquare=[]
    occupiedSquare.append(coord)
    x= coord[0]
    y= coord[1]

    # Checking Horizontal direction
    for offsetX in range(1,5):
        newCoord = [x+offsetX,y]
        if newCoord[0]>=0 and newCoord[0]<=4:
            occupiedSquare.append(newCoord)
        else:
            break
        
    for offsetX in range(1,5):    
        newCoord = [x-offsetX,y]
        if newCoord[0]>=0 and newCoord[0]<=4:
            occupiedSquare.append(newCoord)
        else:
            break

    # Checking Vertical direction   
    for offsetY in range(1,5):
        newCoord = [x,y+offsetY]
        if newCoord[1]>=0 and newCoord[1]<=4:
            occupiedSquare.append(newCoord)
        else:
            break
        
    for offsetY in range(1,5):    
        newCoord = [x,y-offsetY]
        if newCoord[1]>=0 and newCoord[1]<=4:
            occupiedSquare.append(newCoord)
        else:
            break
    # Checking diagonal in SE direction
    for offset in range(1,5):
        newCoord = [x+offset,y+offset]
        if newCoord[0]>=0 and newCoord[0]<=4 and newCoord[1]>=0 and newCoord[1]<=4:
            occupiedSquare.append(newCoord)
        else:
            break
    # Checking diagonal in NW direction  
    for offset in range(1,5):    
        newCoord = [x-offset,y-offset]
        if newCoord[0]>=0 and newCoord[0]<=4 and newCoord[1]>=0 and newCoord[1]<=4:
            occupiedSquare.append(newCoord)
        else:
            break
    # Checking diagonal in NE direction   
    for offset in range(1,5):
        newCoord = [x-offset,y+offset]
        if newCoord[0]>=0 and newCoord[0]<=4 and newCoord[1]>=0 and newCoord[1]<=4:
            occupiedSquare.append(newCoord)
        else:
            break
    # Checking diagonal in SW direction   
    for offset in range(1,5):    
        newCoord = [x+offset,y-offset]
        if newCoord[0]>=0 and newCoord[0]<=4 and newCoord[1]>=0 and newCoord[1]<=4:
            occupiedSquare.append(newCoord)
        else:
            break

    return occupiedSquare

def findAllUniqueOccupiedSquares(cat1Squares, cat2Squares, cat3Squares):

    allOccupiedSquares = cat1Squares

    for square in cat2Squares:
        matchFlag = False
        for existingSquare in allOccupiedSquares:
            if square[0] == existingSquare[0] and square[1] == existingSquare[1]:
                matchFlag = True
                break
        if not matchFlag:
            allOccupiedSquares.append(square)
            
    for square in cat3Squares:
        matchFlag = False
        for existingSquare in allOccupiedSquares:
            if square[0] == existingSquare[0] and square[1] == existingSquare[1]:
                matchFlag = True
                break
        if not matchFlag:
            allOccupiedSquares.append(square)
            
    return allOccupiedSquares

# Create board
board = []
for x in range(5):
    for y in range(5):
        board.append([x,y])
print("The board co-ordinates are:")
print(board)

combo = 0
solution = 0
 
for cat1 in range(25):

    boardAfterCat1 = list(range(0,25))
    boardAfterCat1.remove(cat1)
    
    for cat2 in boardAfterCat1:
        boardAfterCat2 = boardAfterCat1[:]
        boardAfterCat2.remove(cat2)

        for cat3 in boardAfterCat2:
            combo +=1
            
            cat1Squares = findOccupiedSquares(board[cat1])
            cat2Squares = findOccupiedSquares(board[cat2])
            cat3Squares = findOccupiedSquares(board[cat3])

            allOccupiedSquares = findAllUniqueOccupiedSquares(cat1Squares,cat2Squares,cat3Squares)
            
            #print(str(combo)+" This solution has " +str(len(allOccupiedSquares))+" squares")
            
            if (25-len(allOccupiedSquares)) ==5:
                print("\n************Found a solution, cats are positioned at:")
                print(board[cat1])
                print(board[cat2])
                print(board[cat3])
                solution +=1
                
print("Found a total of " + str(solution) + " solutions in all " +str(combo)+ " possible combinations!")
print("As the cats are not unique, there is a total of " + str(int(solution/6)) + " unique solutions!")
