high_blood=[]
low_blood=[]
average=[]
path='data.txt'
with open(path) as f:
    for line in f.readlines():
        s=line.split(", ")
        high_blood.append(str(s[0]))
        low_blood.append(str(s[1]))
        low="".join(low_blood)
        t=low.split("\n")
blood=list(map(int,high_blood))
heart=list(map(int,t))
print(low)

sumblood=sum(blood)
averagesumblood=sumblood/7
print("血壓平均: %.2f" % averagesumblood)
print(f"血壓最高:{max(blood)}")
print(f"血壓最低:{min(blood)}")

sumheart=sum(heart)
averagesumheart=sumheart/7
print("心跳平均: %.2f" % averagesumheart)
print(f"心跳最高:{max(heart)}")
print(f"心跳最低:{min(heart)}")