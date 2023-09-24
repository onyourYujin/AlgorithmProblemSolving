def solution(n):
    m = n+1
    while 1:
        if bin(n)[2:].count("1") == bin(m)[2:].count("1"):
            return m
        m += 1