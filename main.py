from wordhandling import gamestate

from getwords import getword

word=getword()
game=gamestate(word)


DIVLINE='+=============++=============+'
tablehead='|    Guess    ||   Result    |'
print(DIVLINE)
print(tablehead)
print(DIVLINE)
while True:
    
    game.inputguess()
