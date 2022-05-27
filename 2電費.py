a=int(input("請輸入電"))
b=a*2.1
c=(a-120)*3.02+120*2.1
e=(a-330)*4.39+120*2.1+210*3.02
f=(a-500)*4.97+120*2.1+210*3.02+170*4.39
g=(a-700)*5.63+120*2.1+210*3.02+170*4.39+150*5.63
c1=(a-120)*2.68+120*2.1
e1=(a-330)*3.61+120*2.1+210*2.68
f1=(a-500)*4.01+120*2.1+210*2.68+170*3.61
g1=(a-700)*4.50+120*2.1+210*2.68+170*3.61+150*4.01
if a<120:
    print("summer"+str("%.2f"%(b)))
    print("non-summer"+str("%.2f"%(b)))
elif a>121 and a<330:
    print("summer"+str("%.2f"%(c)))
    print("non-summer"+str("%.2f"%(c1)))
elif a>331 and a<500:
    print("summer"+str("%.2f"%(e)))
    print("non-summer"+str("%.2f"%(e1)))
elif a>501 and a<700:
    print("summer"+str("%.2f"%(f)))
    print("non-summer"+str("%.2f"%(f1)))
else:
    print("summer"+str("%.2f"%(g)))
    print("non-summer"+str("%.2f"%(g1)))