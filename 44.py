a=int(input("輸入班級數量:"))
max_value=0
for i in range(a):
    b=(input("輸入班級人數:"))
    for j in b:
        j=int(''.join(b))
        if(j>(max_value)):
            max_value=j
print(max_value)