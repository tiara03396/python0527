
a=int(input("輸入第一行正整數:"))
b=input("輸入第二行數列中的數字:").split(" ")
max=0
aa=0
for i in range(len(b)):
    b[i]=int(b[i])
    if (b.count(b[i])>max):
        max=b.count(b[i])
        aa=b[i]
if max==1:
    print("每個數字剛好只出現一次")
else:
        print("最大出現次數的數字為:"+str(aa))
        print("出現次數為:",max)