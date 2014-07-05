# """ This is Jake's text adventure game """
# print ('''hello and welcome to the world of pokemon. my name is pro. oak people call me the pokemon prof. 
# this world is world is inhabited with creatures called pokemon.
#  many people use them for fights others keep them as pets. i study pokemon as a profesion.
# ''') 

# name = input("So what is your name??\n> ")

# print ("so your name is " + name)

health = 20
attack = 11
defense = 11
speed = 11
special = 8





while True:
	print("your pikachu's health is " + str(health))
	print("your pikachu's attack is " + str(attack))
	print("your pikachu's defense is " + str(defense))
	print("your pikachu's speed is " + str(speed))
	print("your pikachu's special is " + str(special))



	action = input("go up down left or right ")

	print ("what would you like to do " + action)

	if action == "something else":
		print ("Oak: this isn't the the time to do that")

	elif action == "up":
		print("you went forward")

	elif action == "down":
	    print("you went south")

	elif action == "pick something up":
	    print("you got an item")


	elif action == "go in tall grass":
	    print("wild rattata appered go pikachu")

	elif action == "use thundershock":
	    print("rattata lost 5 hp. wild rattata used tackle. pikachu lost 4 hp.")
	    health = health - 4

	elif action == "use potion":
	    print("pikachu was healed by 20 hp")
	    health = health + 20

	elif action == "use growl":
	    print("pikachu used growl. wild rattata's attack went down. wild rattata used tail whip. pikachu's defense went down.")
	    defense = defense - 1

	elif action == "double team":
	    print("pikachu used double team. pikachu's speed went up. wild rattata used hyper fang.")
	    health = health - 6
	    speed = speed *2

	elif action == "run":
	    print("you got away safely.")

	elif action == "thunder wave":
	    print("pikachu used thunder wave. wild rattata is parlized. rattata used tunder wave")
	    speed = speed /2

	else:
		print("Oak: this isn't the time to do that")
	