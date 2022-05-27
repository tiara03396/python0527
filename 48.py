dict={"dog":"狗","cat":"貓","bear":"熊","snake":"蛇"}
n=input("輸入欲查詢單字:")
s=dict.get(n)
if s==None:
    print("無單字")
else:
    print(n+"中文意思為"+str(dict[n]))