a=b=n=0
ans="1234"
guess=str(input("輸入數字"))
for i in guess:
    if guess.index(i)==ans.index(i):
        a+=1
    else :
        b+=1
print(a,"A",b,"B")