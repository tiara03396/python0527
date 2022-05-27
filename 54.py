from decimal import ROUND_UP
import math


a=float(input("請輸入路程公里數:"))
if a<=1.5:
    print("所需車資為:75")
else:
    b=(a-1.5)
    b1=(math.ceil(b/0.25))
    b2=(b1*5+75)
    print("所需車資為:",b2)

