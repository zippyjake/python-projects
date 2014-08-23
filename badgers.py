import time

def badgers():
    badgers = 1
    while badgers <= 12:
        print(badgers,'badgers')
        badgers += 1
        time.sleep(0.3)

def mushroom ():
    for mushroom in range(2):
        print(mushroom+1,'mushroom')
        time.sleep(0.7)
        
badgers()
mushroom ()
