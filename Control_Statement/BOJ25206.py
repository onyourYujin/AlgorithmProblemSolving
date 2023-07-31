standard = {"A+":"4.5","A0":"4.0","B+":"3.5","B0":"3.0","C+":"2.5","C0":"2.0","D+":"1.5","D0":"1.0","F":"0.0"}
sum = 0
result = 0
for x in range(20):
    subject, score, grade = input().split()
    if grade == "Pass":
        pass
    else:
        sum +=float(score)
        gpa=float(score)*float(standard[grade])
        result+=gpa
print(f'{result/sum:.6f}')