def read_class5():
    class5=[]
    f=open('5.10_1.txt','r')
    while True: 
        line=f.readline() 
        if len(line)==0: # Zero length indicates EOF 
            break 
        class5.append(line.split())
    return class5
    f.close()

#main
class510=[]
class510=read_class5()
print(class510)
