a=int(input("Enter number A: "))
b=int(input("Enter number B: "))
c=int(input("Enter number C: "))

if a>b:
    if a>c:
        greatest=a
    else:
        greatest=c
else:
    if b>c:
        greatest=b
    else:
        greatest=c


print("Greatest number is  = ",greatest)
