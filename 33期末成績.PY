list1=["國文","英文","微積分","體育","程式設計"]
list=[]
for i in range(len(list1)):
    list.append(int(input("輸入"+list1[i]+"的分數")))
avg=sum(list)/len(list1)
print("平均分數:%.2f"%avg)
print("最高分科目:",list1[list.index(max(list))],max(list))
print("最低分科目:",list1[list.index(min(list))],min(list))
