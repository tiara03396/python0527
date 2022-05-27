m=int(input("輸入月份"))
d=int(input("輸入日"))
s1=(m*2+d)%3
if s1==0:
    print("普通")
elif s1==1:
    print("吉")
else:
    print("大吉")
