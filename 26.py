while True:
    a=input("檢測的字串(end 結束):")
    
    if a=="end":
        break
    else:
        sum=0
        a=list(a)
        b=input("檢測的單一字元:")
        if b==None:
            print("重新輸入")
        else:
            for i in range(len(a)):
                if a[i]==b:
                    sum+=1
            print(sum)
