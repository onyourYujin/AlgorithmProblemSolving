while True:
    n = int(input())
    if n == -1:
        break
    lst = []
    for x in range(1,n):
        if n % x == 0:
            lst.append(x)
    if sum(lst) == n:
        print(n," = "," + ".join(str(i) for i in lst),sep="")
    else:
        print(f"{n} is NOT perfect.")