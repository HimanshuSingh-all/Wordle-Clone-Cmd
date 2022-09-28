
from random import randint
def getword()->str:
    fname='sgb-words.txt'
    
    with open(fname) as hand:
        num=randint(1,5757)
        for i,word in enumerate(hand):
            if i+1==num:
                return word.split()[0]


