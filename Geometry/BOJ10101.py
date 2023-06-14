A=int(input())
B=int(input())
C=int(input())
if A==B==C:
    print("Equilateral")
elif A+B+C == 180:
    if A==B or A==C or B==C:
        print("Isosceles")
    else:
        print("Scalene")
elif A+B+C != 180:
    print("Error")