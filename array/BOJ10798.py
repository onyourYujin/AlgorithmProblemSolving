array = [input() for i in range(5)]
for column in range(15):
    for row in range(5):
        if column < len(array[row]):
            print(array[row][column], end ='')