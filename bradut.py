with open("globulet.txt",'r')as f:
    a=f.readline()
b=int(a)+3
c=int(a)+b-3
with open("bradut.txt",'w')as f:
    a=f.writelines(str(int(a)+b+c))
   

