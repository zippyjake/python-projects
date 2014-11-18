#Luigi's Mansion
from random import randint
print("Luigi's Mansion")
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print("Three doors ahead... ")
    print("A ghost is behind one.")
    print("Witch door do you open?")
    door = input("1, 2, 3?")
    door_num = int(door)
    if door_num == ghost_door:
        print("KING BOO!")
        feeling_brave = False
    else:
        print("Lit Room.")
        print("You went to the next room.")
        score = score + 1
print("Run away")
print("GAME OVER! You scored", score)
