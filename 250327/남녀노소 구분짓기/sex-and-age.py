s=int(input())
age=int(input())

if age>=19:
    if s==1:
        print("WOMAN")
    else:
        print("MAN")

if age<19:
    if s==1:
        print("GIRL")
    else:
        print("BOY")