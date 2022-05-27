n = int(input("請輸入一個正整數(<10) : "))
for i in range(n+1):
    k = i
    for j in range(i):
        print("%2d" % (k+k*j), end=" ")
    print()