a=int(input("搭了幾次電梯:"))
n=1
sum=0
for i in range(0,a):
    b=int(input(i+1))
    if b-n>0:
        sum=(b-n)*20+sum
        n=b
    elif b-n<0:
        sum=(n-b)*10+sum
        n=b
print(sum,"元")

    
