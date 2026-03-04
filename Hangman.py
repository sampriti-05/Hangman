import random
global s
global ans
L=[]
we=[]
wh=[]
wm=[]
print("Welcome, brave guesser! \n Your mission is simple — uncover the secret word chosen by the machine. \n But beware… you only get a few lives!")
f1=open("Words.txt","r")
for i in f1.readlines():
    i.rstrip()
    L.append(i)
for i in L:
    if len(i)>=7:
        wh.append(i)
    elif len(i)<7 and len(i)>=5:
        wm.append(i)
    else:
        we.append(i)
def con():
    global s
    s=""
    p=input("Do You Want To Continue: [Y/N]: ")
    if p.upper()=="Y":
        F()
    elif p.upper()=="N":
        print("Thanks For Playing !")
    else:
        print ("Enter valid answer")
        con()
def F():
    global d
    global ans
    ans=input("Ready to play [Y/N] ? : ")
    if ans.upper()=="Y":
        print("Choose a level: \n 1. Easy \n 2. Medium \n 3. Hard")
        def clev():
            lev=input ("Enter desired level [E/M/H]: ")
            if lev.upper()=="E":
                Easy()
            elif lev.upper()=="M":
                Medium()
            elif lev.upper()=="H":
                Hard()
            else:
                print("Please Enter valid level")
                clev()
        clev()
    elif ans.upper()=="N":
        print("Maybe next time. \n Thanks for visiting !!")
    else :
        print("Please Enter valid answer")
        F()
def Hard():
    global d
    global L
    print("Be careful you only get 4 lives")
    global lives
    lives=4
    global word
    global k
    k=random.randint(1,len(wh))
    word=wh[k].strip()
    d=len(word)*"_"
    L1= list(d)
    print("The word looks like: ", d)
    def guess():
        global d
        global L
        global lives
        global s
        global word
        while lives>0:
           g=input("Guess a letter:")
           if g.upper() in word.upper():
               for i in range(0, len(word)):
                   if word[i].upper()==g.upper():
                       L1[i]=g
               s="".join(L1)
               print(s)
               print()
               if s.upper()==word.upper():
                   lives=-1
                   print("Congratulations, You Won!! The word was ",word)
                   con()
                   break
               else:
                   guess()
           else:
               lives=lives-1
               if lives==0:
                      print(" Lives left:0 \n Oops! Ran out of lives :( \n The word was:",word)
                      con()
                      break
               else:
                      print("Oops Wrong Guess ! \n Lives Left:",lives)
                      guess()
    guess()   
def Medium():
    global d
    global L
    print("Be careful you only get 3 lives")
    global lives
    lives=3
    global word
    global k
    k=random.randint(1,len(wm))
    word=wm[k].strip()
    d=len(word)*"_"
    L1=list(d)
    print("The word looks like: ",d)
    def guess():
        global d
        global L
        global lives
        global s
        while lives>0:
           g=input("Guess a letter:")
           if g.upper() in word.upper():
               for i in range(0, len(word)):
                   if word[i].upper()==g.upper():
                       L1[i]=g
               s="".join(L1)
               print(s)
               print()
               if s.upper()==word.upper():
                  lives=-1
                  print("Congratulations, You Won!! The word was ",word)
                  con()
                  break
               else:
                  guess()
           else:
               lives=lives-1
               if lives==0:
                      print(" Lives left:0 \n Oops! Ran out of lives :( \n The word was:",word)
                      con()
                      break
               else:
                      print("Oops Wrong Guess ! \n Lives Left:",lives)
                      guess()
               
    guess()
def Easy():
    global d
    global L
    print("Be careful you only get 5 lives")
    global lives
    lives=5
    k=random.randint(0,len(we))
    word=we[k].strip()
    d=len(word)*"_"
    L1= list(d)
    print("The word looks like: ", d)
    def guess():
        global d
        global L
        global lives
        global s
        while lives>0:
           g=input("Guess a letter:")
           if g.upper() in word.upper():
               for i in range(0, len(word)):
                   if word[i].upper()==g.upper():
                       L1[i]=g
               s="".join(L1)
               print(s)
               print()
               if s.upper()==word.upper():
                  lives=-1
                  print("Congratulations, You Won!! The word was ",word)
                  con()
                  break
               else: 
                  guess()
           else:
                  lives=lives-1
                  if lives==0:
                      print(" Lives left:0 \n Oops! Ran out of lives :( \n The word was:",word)
                      con()
                      break
                  else:
                      print("Oops Wrong Guess ! \n Lives Left:",lives)
                      guess()
    guess()
    
F()




