#test every day
def cls(): 
    print("\n"*50) 
#2017.9.17
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
#2017.9.12 
ts=0
ctj_tmp=ctj=[]
fi=open("tkdatctjout.txt", 'r',encoding="utf-8") #read last test's wrong artical
ctj_tmp=fi.read().strip().split("\n")
ctj=list(set(ctj_tmp))
ctj.sort()
fi.close()
#if ctj[0]=="":
#    ctj[0]="1"
fi=open("tkdatxztout.txt", 'r',encoding="utf-8") 
fo=open("tkdatctjout"+date_name+".txt", 'w',encoding="utf-8")

while True: 
    aa=fi.readline() 
    if aa=="" :break 
    tkdat.append([aa.split("|")]) 
fi.close() 
print(ctj)
for i in tkdat: 
    cls()
    if int(i[0][0])<int(ctj[len(ctj)-1]) and i[0][0]+" " not in  ctj :
        #print(i[0][0],(ctj[len(ctj)-1]))
        continue
    #else :print("aaaaa",i[0][0])
    #print(ctj)
    #break
      
    print("总序号:",i[0][0],"总题数：",ts,"错：",wr,"对：",ri,"\n\n") 
    print(i[0][1],i[0][2],"\n") 
    print(i[0][3][:i[0][3].find("B")-1].strip(),"\n\n",\
          i[0][3][i[0][3].find("B"):i[0][3].find("C")].strip(),"\n\n",\
          i[0][3][i[0][3].find("C"):i[0][3].find("D")].strip(),"\n\n",\
          i[0][3][i[0][3].find("D"):].strip(),"\n\n")

    ans=input("请选择[Q :exit]:") 
    if ans.upper().strip()=="Q":
#        fo.write("\n"+i[0][0])    #写入当前题号
        ctj.append(i[0][0].strip())
        break 
    elif ans.upper().strip()==i[0][4].upper().strip(): 
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
        print(i[0][4]) 
        input("input any key for NEXT....") 
        wr=wr+1 
        ts=ts+1 
        #fo.write("\n"+i[0][0])
        ctj.append(i[0][0].strip())
        for i in ctj:
            if i !="" :fo.write(i+"\n")
        continue 
cls() 
print("总题数：",ts,"\n","错：",wr,"对：",ri,"\n\n")
ctj_tmp=list(set(ctj))
ctj_tmp.sort()
for i in ctj_tmp:
    if i !="" :fo.write(i.strip()+"\n")
fo.close() 

