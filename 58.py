a10=int(input("輸入第1個數字"))
a1=int(input("輸入第2個數字"))
a2=int(input("輸入第3個數字"))
a3=int(input("輸入第4個數字"))
a4=int(input("輸入第5個數字"))
a5=int(input("輸入第6個數字"))
a6=int(input("輸入第7個數字"))
a7=int(input("輸入第8個數字"))
a8=int(input("輸入第9個數字"))
a9=int(input("輸入第10個數字"))
list=[a10,a1,a2,a3,a4,a5,a6,a7,a8,a9]

max_1=max(list)
list.remove(max_1)
max_2=max(list)
list.remove(max_2)
max_3=max(list)
min_1=min(list)
list.remove(min_1)
min_2=min(list)
list.remove(min_2)
min_3=min(list)
print("最大的三個數字分別為:"+str(max_1)+","+str(max_2)+","+str(max_3))
print("最小的三個數字分別為:"+str(min_1)+","+str(min_2)+","+str(min_3))
