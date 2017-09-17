#2017.9.12   
tkdat=[] 
tend='0' 
tg3_last=tg3="" 
tx=th=tg1=tg2=tg3=da="" 
thglobal=thglobal1=0 
fi= open("tkdat.txt", 'r',encoding="utf-8") 
fo= open("tkdatxztout.txt", 'w',encoding="utf-8")
fo1= open("tkdatpdtout.txt", 'w',encoding="utf-8") 
while True: 
    line = fi.readline() 
    if line=="" :break 
    if "判断题" in line: 
#        print("判断题begin:") 
        while True: 
            line = fi.readline() 
            line = line.strip()                      #去掉每行头尾空白   
            if line==""  : 
                break 
            if not len(line) or line.startswith('#'):      #判断是否是空行或注释行 
                continue 
            if "．" in line : 
                th=line[:line.find("．")] 
                tg=line[line.find("．")+1:line.find("（")] 
                da=line[line.find("（"):] 
            elif "." in line : 
                th=line[:line.find(".")] 
                tg=line[line.find(".")+1:line.find("（")] 
                da=line[line.find("（"):] 
            if "√" in da :da="0" 
            elif "×" in da :da="1" 
            else :da="9" 

            #tkdat.append([th,tg,da])
            thglobal1=thglobal1+1
            fo1.write(str(thglobal1)+"|"+th+"|"+tg+"( )"+"|"+da+"\n" ) 
            th="" 
#           print("判断题begin:",th,tg,da) 




    elif "单选题" in line  or "多选题" in line  : 
        print("单选题begin")
        if "单选题" in line:tx="S"
        else :tx="M"
        while True: 
            line=fi.readline().strip() 
            if line==""  or (("．" not in line) and ("." not in line)) :                 #处理最后一题的答案 
#                print("xzt3",th,tg1,tg2) 
                tend='0' 
                thglobal=thglobal+1 
                #tkdat.append([thglobal,th,tg1+"(  )"+tg2,tg3,da]) 
                if line!="": 
                    fo.write(str(thglobal)+"|"+tx+th+"|"+tg1+"( )"+tg2+"|"+tg3+"|"+da+"\n" ) 
                th=tg1=tg2=da=tg3="" 
                print("break1") 
                break 
            elif  ("．" in line) or ("." in line): 
                line = line.strip()                             #去掉每行头尾空白 
#                print("xzt1:",line) 
                if not len(line) or line.startswith('#'):       #判断是否是空行或注释行   
                    continue     
                if "．" in line: 
                    if tend=='1' : 
                        th_last=th 
                        tg1_last=tg1 
                        da_last=da 
                        tg2_last=tg2 
                        tg3_last=tg3 
                        tend='2' 
                    th=line[:line.find("．")].strip()         #注意题号的点和选项的点是不同的 
                    tg1=line[line.find("．")+1:line.find("（")].strip() 
                    da=line[line.find("（")+1:line.find(" ）")].strip() 
                    tg2=line[line.find("）")+2:].strip() 
#                    print("T branch.",th,"|",tg1,"|",tg2,"|",da) 
                elif "." in line : 
                    th1=line[:line.find(".")].strip() 
                    if th1 in ("A","B","C","D") : 
                        tg3=tg3+line 
                        tend='1' 
#                        print("Answer branch:",tg3,tend) 
                        continue 
                    else : 
                        th_last=th 
                        tg1_last=tg1 
                        da_last=da 
                        tg2_last=tg2 
                        tg3_last=tg3 
                        tend='2' 
                        th=line[:line.find(".")].strip()     #有些题又用的是这种点 
                        tg1=line[line.find(".")+1:line.find("（")].strip() 
                        da=line[line.find("（")+1:line.find(" ）")].strip() 
                        tg2=line[line.find(" ）")+2:].strip() 
#                        print("T1 branch.",th,tg1,tg2) 
                if tend=='2':    #读完选项后再组装成一题 
#                    print("xzt2",th_last,tg1_last,tg2_last) 
                    tend='0' 
                    thglobal=thglobal+1 
                    #tkdat.append([str(thglobal),th_last,tg1_last+"( )"+tg2_last,tg3_last,da_last]) 
                    if th_last!="": 
                        fo.write(str(thglobal)+"|"+tx+th_last+"|"+tg1_last+"( )"+tg2_last+"|"+tg3_last+"|"+da_last+"\n" ) 
                    tg3="" 
            else: 
                print("break2") 
                break 
    else: 
        line=line.strip() 
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行 
            continue 
        print("line:",line) 
        #tkdat.append([line]) 
fi.close() 
fo.close()
fo1.close()

