for i in range(6):
    for j in range(5-i):#4,3,2,1,0
        print("",end="")
    for n in range(i):
        print("*",end="")
    print()
for i in range(4,0,-1):
    for k in range(-i+5):
        print(" ",end="")
    for n in range(i):
        print("*",end="")
    for j in range(5-i):
        print("",end="")
    print()