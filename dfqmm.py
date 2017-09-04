# qz b--blue  w--white  1-不可见  0-可见

def start_game_init():
     global qz
     for i in range(12):
          qz_tmp=[(i,'w'),'1']
          qz.append(qz_tmp)
          qz_tmp=[(i,'b'),'1']
          qz.append(qz_tmp)
     #99为连字符
     qz=qz+[[(99,'w'),'1'],[(99,'b'),'1']]
     print("func1:",qz,":func1")

def fapai():
     global qz,player1,ai_player
     for i in range(4):
          player1=player1+[qz.pop(random.randrange(len(qz)))]
          ai_player=ai_player+[qz.pop(random.randrange(len(qz)))]
     #player1 的牌设为可见
     for j in player1:
          j[1]='0'
     player1.sort()
     ai_player.sort()
     
def  display_paiju():
     print("\n"*50)
     print("ai_player 的牌：")
     #print(ai_player)
     for j in ai_player:
          if j[1]=='1':
                     print("( **,",j[0][1],")",end=" ")
          else :
                print("(",j[0][0],",",j[0][1],")",end=" ")

     print("\n"*5)
     print("待摸牌：")
     print("剩余：",len(qz))
     tmp_qz=[]
     for k in qz:tmp_qz.append(k[0][1])
     print ("b:", tmp_qz.count('b'))
     print ("w:", tmp_qz.count('w'))             
     

     print("\n"*5)
     print("player1 的牌：")
     #print(player1)
     for j in player1:
          if j[1]=='1':
                     print("( **,",j[0][1],")",end=" ")
          else :
                print("(",j[0][0],",",j[0][1],")",end=" ")

        
def deal_player_99():
     """
     ck_input_ok=0
     while ck_input_ok:
          i=input ("连字符位放哪：")
          if int(i)<0 or  int(i)>len(player1):
               print("Input error,out of range")
               break
          else :
               input_ok=1
               for j in qz_99:
                    if j in player1:
                         player1.insert(int(i),j)
                         player1.pop(-1)
                         break
     """
     #发牌时随机安放99
     if (99,'w','0') in player1 :
          player1.pop(player1.index((99,'w','0')))
          player1.insert(random.randrange(len(player1)),(99,'w','0'))
     elif (99,'b','0') in player1 :
          player1.pop(player1.index((99,'b','0')))
          player1.insert(random.randrange(len(player1)),(99,'b','0'))
          
     if (99,'w','1') in player1 :
          player1.pop(player1.index((99,'w','1')))
          player1.insert(random.randrange(len(player1)),(99,'w','1'))
     elif (99,'b','1') in player1 :
          player1.pop(player1.index((99,'b','1')))
          player1.insert(random.randrange(len(player1)),(99,'b','1'))

def  is_player_has_99():
     global qz_99
     for i in qz_99:
          if i in player1:return 1
          else: return 0
def  get_new():
     global qz_new
     global game_over
     if len(qz)==0 :
          print("finished\n")
          game_over=1
     else:
          qz_new=qz.pop(random.randrange(len(qz)))
          print("\nYou got:","(",qz_new[0][0],",",qz_new[0][1],")\n")
def guess():
     global qz_guess
     i=input("input positon and nubmer such as '3 10':")
     for j in i.split(" "):  qz_guess.append(int(j))
def judge():
     a = []
     for j in ai_player:a.append(j[1])
     if a.count('1')=='0':
          game_over=1
          print("You Win,gameOver!")
     if ai_player[qz_guess[0]][0][0]==qz_guess[1]:
          ai_player[qz_guess[0]][1]='0'
          input("Right,please input any key...\n")
      
     else:
          qz_new[1]='0'
          player1.append(qz_new)
          player1.sort()
          


     
import random
qz=[]
qz_99=[[(99,'b'),'0'],[(99,'b'),'1'],[(99,'w'),'0'],[(99,'w'),'1']]
qz_new=[]
qz_guess=[]
player1=[]
ai_player=[]
game_over=0

start_game_init()
fapai()
display_paiju()
while game_over!=1:
     if is_player_has_99() :  deal_player_99()
     display_paiju()
     get_new()
     guess()
     judge()
     input("please input any key")
     qz_new=[]
     qz_guess=[]
          
          
     
           
           
"""
print(qz)
print(player1)
print(ai_player)
"""
