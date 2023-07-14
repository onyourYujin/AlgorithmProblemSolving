while 1:
    triangle = list(map(int,input().split()))
    triangle.sort() 
    a=triangle[0]
    b=triangle[1]
    c=triangle[2]
    if triangle[0] == 0:
        break
    elif a+b<=c:
        print("Invalid")
    else:
        if a==b==c :
            print("Equilateral")
        elif (a==b and a!=c) or (a==c and b!=c) or (b==c and a!=b):
            print("Isosceles")
        elif a!=b!=c:
            print("Scalene")