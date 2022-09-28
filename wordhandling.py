import msvcrt as ge
import os
from types import NoneType
os.system('color')

DIVSTR='+=============++=============+'
guessline='|             ||              |'
def wordtomap(word:str):

    retmap=dict()

    for index,char in enumerate(word):
        if char not in retmap:
            indict=set()
            indict.add(index)
            retmap[char]=indict
        else:
            retmap[char].add(index)
    return retmap

class gamestate():

    def __init__(self,word,MAXCOUNT=6):

        self.word=[w for w in word] #initialises the word to be guessed
        self.strword=word
        self.counter=0
        self.MAXCOUNT=MAXCOUNT
        self.wmap=wordtomap(word)
        self.win=False

    def disp_guess_result(self,gword:list,retlist:list,count:int)->bool:

        print('||  ', end="")
        for i,w in enumerate(gword):
            #TODO :set might not be agreat idea in case we want to handle 2 repeating characters
            try:

                if i in self.wmap[w]:
                    print("\033[92m{}\033[00m".format(w), end=" ")
                    self.wmap[w].remove(i)
                    if not self.wmap[w]:
                        del self.wmap[w] 
                else:
                    print("\033[93m{}\033[00m".format(w), end=" ")

            except KeyError:
                print(w,end=" ")

        print(' |') 
        if gword==self.word:
            self.win=True
            self.gameover(True)
        print(DIVSTR)

    def guesscheck(self,gword):

        retlist=list()
        for i,c in enumerate(gword):
             
            if c in self.wmap:
                retlist.append(self.wmap[c]==i)
            else:
                retlist.append(False)
        self.disp_guess_result(gword,retlist,self.counter)

    def inputguess(self):
        n=0
        word=['|',' ',' ']#[w for w in f"Guess {self.counter+1}: "]
        gword=[]
        for w in word:
            ge.putch(w.encode())

        while True:

            #print ("\033[A                             \033[A",end="")        
            inp=ge.getch()
                
            if inp==b'\x03':
                break

            elif inp==b'\x08':
                #print('bskp dtect') 
                
                if gword:    
                    gword.pop()
                    #word.pop()
                    n=n-1
                   # print ("\033[A \033[A")   
            
            elif inp.decode('ASCII').isalpha():

                gword.append(inp.decode('ASCII'))
                #word.append(inp.decode('ASCII'))
                n+=1 
            print("\r", end="")#    
            for w in word:           
                ge.putch(w.encode())

            for w in gword:
                ge.putch(w.encode())
                ge.putch(b' ')
            if n>=5:
                ge.putch(b' ')
                break

        self.guesscheck(gword)
        self.counter+=1
        if self.counter>=self.MAXCOUNT:
            self.gameover(False)

        self.wmap=wordtomap(self.strword)
    
    def gameover(self,win:bool)->None:
        
        print(DIVSTR)
        if win:
            print(f'Congratulations, you guessed the word {self.strword} in {self.counter} tries!!')
        else:
            print(f'Looks like you lost, the word was {self.strword}')
        raise SystemExit
