N = []
N_Max =[]

for i in range(9):
    lst =  list(map(int,input().split()))
    N.append(lst)
    N_Max.append(max(lst))
print(max(N_Max))

for row in range(9):
  for column in range(9):
    result = N[row][column]
    if max(N_Max) == result :
       print(row+1, column+1)