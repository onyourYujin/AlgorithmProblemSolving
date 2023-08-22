words = [input() for i in range(5)]
for column in range(15):
    for row in range(5):
        if column < len(words[row]):
            print(words[row][column], end =' ')