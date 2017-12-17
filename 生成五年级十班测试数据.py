import random
class5=[]
f=open('5.10.txt','r')
while True: 
    line=f.readline() 
    if len(line)==0: # Zero length indicates EOF 
        break 
    class5.append(line.split())
f.close()
f=open('5.10_1.txt','a')
class5_fs=[]
stu1=[]
for stu in class5:
    stu1=[stu[0],stu[1],random.randint(60,100),random.randint(60,100),random.randint(60,100)]
    class5_fs.append(stu1)
    f.write('20171201'+' '+stu1[0]+' '+stu1[1]+' '+str(stu1[2])+' '+str(stu1[3])+' '+str(stu1[4])+'\n')
f.close()

yw=sx=yy=0
for stu in class5_fs:
    #print(stu[0],stu[1],stu[2]+stu[3]+stu[4],(stu[2]+stu[3]+stu[4])/3)
    yw = stu[2]+yw
    sx = stu[3]+sx
    yy = stu[4]+yy
    
print(yw+sx+yy,(yw+sx+yy)/30/3)
