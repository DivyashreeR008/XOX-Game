import random 
lst=[1,2,3,4,5,6,7,8,9]
b=[1,2,3,4,5,6,7,8,9]
ch=[]
print('*********************************')
for i in lst:
      if i ==3 or i==6 or i==9:
                print(i,'\n')
      else:
                print(i,end='|')
print('*********************************')             
def shape(n,m,z,w): # function to display
  global lst
  if z ==1: 
    if n in ch:
          print('*********************************')
          print('You  are cheating ,please try again' )
          if m==p1:
              print('*********************************')
              game(0,w)
          elif m==p2:
              game(1,w)
          
    elif n in [1,2,3,4,5,6,7,8,9] and w != 5:                
         lst[n-1]=m    
         ch.append(n)
         print('*********************************')
         for j,i in enumerate(lst):
                 if j==2 or j==5 or j==8:
                        print(i,'\n')
                 else:
                        print(i,end='|') 
         print('*********************************')
    elif n in [1,2,3,4,5,6,7,8,9] and w == 5:
         random.shuffle(lst)
         lst[lst.index(n)]=m    
         ch.append(n)
         print('*********************************')
         for j,i in enumerate(lst):
                 if j==2 or j==5 or j==8:
                        print(i,'\n')
                 else:
                        print(i,end='|')        
         print('*********************************')               
    else:
         print("You exceeded the given range")
         if m==p1:
              game(0,w)
         elif m==p2:
              game(1,w)
  else:                           
    if n in ch:
          print('*********************************')
          print('You  are cheating ,please try again' )
          print('*********************************')
          if m==p1:
              ai(0,w)
          elif m==p2:
              ai(1,w)
          
    elif n in [1,2,3,4,5,6,7,8,9] and w != 5:               
         lst[n-1]=m    
         ch.append(n)
         print('*********************************')
         for j,i in enumerate(lst):
                 if j==2 or j==5 or j==8:
                        print(i,'\n')
                 else:
                        print(i,end='|')
         print('*********************************')
    elif n in [1,2,3,4,5,6,7,8,9] and w == 5:
         random.shuffle(lst)
         e=lst.index(n)             
         lst[e]=m    
         ch.append(n)
         print('*********************************')
         for j,i in enumerate(lst):
                 if j==2 or j==5 or j==8:
                        print(i,'\n')
                 else:
                        print(i,end='|')    
         print('*********************************')
    else:
         print("You exceeded the given range")
         if m==p1:
              ai(0,w)
         elif m==p2:
              ai(1,w)            
          
def game(i,k):#function to get input 
    if str(i) in '02468':
           print('It\' s time for player no : 1')    
           n =int(input('Enter the position no :'))        
           shape(n,p1,1,k)           
    elif str(i) in '13579':
           print('It\' s time for player no : 2')    
           n =int(input('Enter the position no :'))
           shape(n,p2,1,k) 
    

def start(v,k): #function to start 
      for i in range(0,9):
         if v==0:   
            game(i,k)
            u=win(i)
            if u==1:
                break 
         else:
            ai(i,k)
            u=win(i)
            if u==1:
                break 
            
      else:
            print('*********************************')
            print(" Game goes to draw, no one wins , please try again")
            print('*********************************')
      conn(k)

def conn(k):#function to continue 
    global lst, p1,p2,ch,b
    lst=[1,2,3,4,5,6,7,8,9]
    b=[1,2,3,4,5,6,7,8,9]
    ch=[]
    print('*********************************')
    c=input("""Hint:  y -->Continue with  the same variables,  e -->Continue by exchanging our variables , q -->quit
    Do you want to continue :""")
    print('*********************************')
    if c=="y" or c=="Y":
        
        if s=="y" or s=='Y':
            start(0,k)
        elif s =="n" or s=='N':
            start(1,k)
                 
    elif c=="e" or c=="E":
        (p1,p2)=(p2,p1)
        if s=="y" or s=='Y':           
            start(0,k)
        elif s =="n" or s=='N':
            start(1,k)
    elif c=="q" or c=="Q":
        print("You ended this program ,Thank you")
    else:
        print("You entered the invalid input, please try again ")
        conn(k)

        
def win(i): # function to end 
    if lst[0]==lst[1]==lst[2] or lst[6]==lst[7]==lst[8] or lst[0] == lst[3] == lst[6] or lst[2]==lst[5]==lst[8] or lst[3]==lst[4]==lst[5] or lst[1]==lst[4]==lst[7] or lst[0] == lst[4] ==lst[8] or lst[2]==lst[4]==lst[6]:
                 if str(i) in '02468':
                     print('*********************************')
                     print("****** Player 1 win the match *******")
                     print('*********************************')
                     return 1
                  
                 elif str(i) in '13579':
                     print('*********************************')
                     print("****** Player 2  win the match *******")
                     print('*********************************')
                     return 1
                  
                 else:
                     pass
    
def ai(i,k):   #function for ai
       global b
       if str(i) in '02468':
           print('It\' s time for player no : 1, that is you')    
           n =int(input('Enter the position no :'))
           try:
               b.remove(n)
           except ValueError:
               shape(n,p1,0,k)
           else:   
               shape(n,p1,0,k)           
       elif str(i) in '13579':
           print('It\' s time for player no : 2, that is me')
                     
           n =random.choice(b)
           print("I select the position no :",n)
           try:
               b.remove(n)
           except ValueError:
               shape(n,p2,0,k)  
           else:   
               shape(n,p2,0,k)    

print('*********************************')                                                    
s= input("""hint: y--> yes , n-->no
Can you  have another player to play this game: """) 
g=input("""This game have two modes:
    a. Normal mode
    b. Shuffle mode
    So , you should select which mode you want(a or b) :""")
print('*********************************')

if s =='y' or s=='Y':
    print('*********************************')
    p1=input('You are player no: 1 , so please select which you want (X or O) :')
    if p1 =='X' or p1== 'x':
      p1='X'
      p2='O'
    elif p1 =='O' or p1=='o':
      p2='X'
      p1='O'
    else:
      print('Invalid Input')
    if g=='a'   or g=='A':
          start(0,1)
    elif g=="b" or g=='B':
          start(0,5)
elif s =="n" or s=='N':
      #print("Don't  worry I will play with you ")
    print('*********************************')
    p1=input('You are player no: 1 , so please select which you want (X or O) :')
    if p1 =='X' or p1== 'x':
      p1='X'
      p2='O'
    elif p1 =='O' or p1=='o':
      p2='X'
      p1='O'
    else:
      print('Invalid Input')
    if g=='a'   or g=='A':
          start(1,1)
    elif g=="b" or g=='B':
          start(1,5)
else:
      print("Invalid input")
