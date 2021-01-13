with open("input.txt",'r')as f:
    a=f.readline()
with open("output.txt",'w')as f:
    s=f.write(str(int(a)-2)+" "+str(int(a)-1)+" "+a+" "+str(int(a)+1)+" "+str(int(a)+2))
