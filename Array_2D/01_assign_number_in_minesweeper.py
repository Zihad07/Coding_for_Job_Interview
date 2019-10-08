
def mini_sweeper(bombs,num_rows,num_cols):
    # create game field
    gameField = []
    for row in range(num_rows):
        gameField.append([0]*num_cols)
    
    # --------------------------


    for bomb in bombs:
        row_i,col_i = bomb[0],bomb[1]

        # set -1 at bomb location
        gameField[row_i][col_i] = -1
        # print(gameField)

        # increment value arround the bomb location

        for i in range(row_i-1,row_i+2,1):
            for j in range(col_i-1,col_i+2,1):
                if 0 <= i and 0<=j and i<num_rows and j<num_cols and gameField[i][j]!=-1:
                    # inccrement value +1
                    gameField[i][j] += 1
                    # print(gameField);
                    # print((i,j),end=" ")
            # print()
        

    return gameField


# -------------------------------------------------------

def print2d(mylist):
    for eachRow in mylist:
        print(eachRow)
    print("----------------");

result = mini_sweeper([[0,0],[0,1]],3,4)

print2d(result)
result = mini_sweeper([[0,0],[0,1],[1,2]],3,4)

print2d(result)
result = mini_sweeper([[1,1],[1,2],[2,2]],3,4)

print2d(result)


