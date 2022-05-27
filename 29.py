a=input("請輸入字串(用,分開)")
b=input("請輸入字串(用,分開)")
list=a.split(",")
list1=b.split(",")
for i in range(len(b)):
    if list[i]>list1[i]:
        print("贏")
    elif list[i]<list1[i]:
        print("輸")
    else:
        print("合")



