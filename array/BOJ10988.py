N = input()
result = ""
for x in N[::-1]:
    result+=x
if N == result:
    print(1)
else:
    print(0)