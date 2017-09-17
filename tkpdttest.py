#2017.9.17
#test 判断题 every day
def cls(): 
    print("\n"*50) 

cls()
import datetime,os
print(os.getcwd())
date_tmp=str(datetime.datetime.now())
date_name=date_tmp[:10]
print(date_name)

tkdat=[] 
ctj=[] 
ri=0 
wr=0
ts=0
ctj_tmp=ctj=[]
fi=open("tkdatctjpdtout.txt", 'r',encoding="utf-8")
ctj_tmp=fi.read().strip().split("\n")
ctj=list(set(ctj_tmp))
ctj.sort()
fi.close()
print(ctj)

fi=open("tkdatpdtout.txt", 'r',encoding="utf-8") 
fo=open("tkdatctjpdtout"+date_name+".txt", 'w',encoding="utf-8")
while True: 
    aa=fi.readline() 
    if aa=="" :break 
    tkdat.append([aa.split("|")]) 
fi.close() 

for i in tkdat:
    cls()
    if int(i[0][0])<int(ctj[len(ctj)-1]) and i[0][0]+" " not in  ctj :
        continue

    print("总序号:",i[0][0],"总题数：",ts,"错：",wr,"对：",ri,"\n\n")
    print(i[0][1],i[0][2],"\n\n\n\n")

    ans=input("请选择[ 0 Right  1 Worng  Q :exit]:") 
    if ans.upper().strip()=="Q":
        ctj.append(i[0][0].strip())
        break
    elif ans.upper().strip()==i[0][3].upper().strip(): 
        print("Right!") 
        ans=input("input any key for NEXT....")
        if ans.upper().strip()=="A":
            ctj.append(i[0][0].strip())
        ri=ri+1 
        ts=ts+1
        if i[0][0].strip() in ctj :
            ctj.remove(i[0][0])
        continue
    else:
        print("Wrong!") 
        print(i[0][3]) 
        input("input any key for NEXT....") 
        wr=wr+1 
        ts=ts+1 
        #fo.write("\n"+i[0][0])
        ctj.append(i[0][0].strip())
        #for i in ctj:
        #    if i !="" :fo.write(i+"\n")
        continue
cls() 
print("总题数：",ts,"\n","错：",wr,"对：",ri,"\n\n")
ctj_tmp=list(set(ctj))
ctj_tmp.sort()
for i in ctj_tmp:
    if i !="" :fo.write(i.strip()+"\n")
fo.close() 


