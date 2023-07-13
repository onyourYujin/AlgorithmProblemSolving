word = [input() for i in range(5)]
for column in range(15):
    for row in range(5):
        if column < len(word[row]):
            print(word[row][column], end ='')