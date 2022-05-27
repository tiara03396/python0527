a=int(input("月租費"))
b=int(input("通話時間"))
if a==186:
    c1=(round(b*0.09))
    if 372<=c1<205:
        c6=c1*0.8
        print(round(c6))
    elif c1<186:
        print(round(a))
    else:
        c7=c1*0.7
        print(round(c7))
elif a==386:
    c3=(round(b*0.08))
    if 772<=c3<424.6:
        c4=c3*0.8
        print(round(c4))
    elif c3<386:
        print(round(a))
    else:
        c5=c3*0.7
    print(round(c5))
elif a==586:
    c8=round(b*0.07)
    if 1172<=c8<645:
        c9=c8*0.8
        print(round(c9))
    elif c8<586:
        print(round(a))
    else:
        c9=c8*0.7
        print(round(c9))
else:
    c10=round(b*0.06)
    if 1972<=c10<1085:
        c11=c10*0.8
        print(round(c11))
    elif c10<986:
        print(round(a))
    else:
        c12=c10*0.7
        print(round(c12))
