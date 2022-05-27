a=int(input("輸入數字"))
b=int(input("輸入數字"))
c=int(input("輸入數字"))
d1=-b
d2=b**2
d3=4*a*c
d4=(d2-d3)**0.5
dd5=2*a
d5=(d1+d4)/dd5
d6=(d1-d4)/dd5
if d5!=d6:
    print(int(d5))
    print(int(d6))
elif d5==d6:
    print(int(d5))
else:
    print("無解")
