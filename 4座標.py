x=int(input("x"))
y=int(input("y"))
c=(x**2+y**2)
if x==0 and y==0:
    print("原點"+"根號"+str(c))
elif x==0 and y!=0:
    print("Y軸"+"根號"+str(c))
elif x!=0 and y==0:
    print("x軸"+"根號"+str(c))
elif x>0 and y>0:
    print("第一象限"+"根號"+str(c))
elif x>0 and y<0:
    print("第四象限"+"根號"+str(c))
elif x<0 and y<0:
    print("第三象限"+"根號"+str(c))
elif x<0 and y>0:
    print("第二象限"+"根號"+str(c))