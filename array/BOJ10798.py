word_list = [input() for i in range(5)]
for column in range(15):
    for row in range(5):
        if column < len(word_list[row]):
            print(word_list[row][column], end ='')