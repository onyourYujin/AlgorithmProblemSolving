apb = ['c=','c-','dz=','dz=','d-','lj','nj','s=','z=']
word = input()
for x in apb:
      if x in word:
        word = word.replace(x,"a")
print(len(word))