import math
a=int(input("輸入金額:"))
b=a/100#5
c=a%100#98
c1=c/50#1
c2=c%50#48
d1=c2/10#4
d2=c2%10#8
e1=d2/5#1
e2=d2%5#3


s=math.floor(b)+math.floor(c1)+math.floor(d1)+math.floor(e1)+math.floor(e2)
print(math.floor(s))