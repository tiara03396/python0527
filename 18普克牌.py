sum=0
for i in range(5):
    a=input("請輸入五張牌")
    if a=="A":
        sum=sum+1
    elif a=="K":
        sum=sum+13
    elif a=="Q":
        sum=sum+12
    elif a=="J":
        sum=sum+11
    else:
        sum=sum+int(a)
print(sum)