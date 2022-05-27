for i in range(0,7,2):
    for j in range(4-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        if j%2==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(0,7,2):
    for j in range(i+2):
        print("",end=" ")
    for j in range(-2*i+10):
        if j%2==0:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()