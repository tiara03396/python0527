n=int(input("輸入N值"))
list1=list()
for i in range(n):
    name=input("輸入名字:")
    mail=input("輸入mail:")
    list1.append(name)
    list1.append(mail)
m=input("請輸入要查詢電子郵件的姓名")
if m==name:
    print(m+"電子郵件帳號為",mail)

