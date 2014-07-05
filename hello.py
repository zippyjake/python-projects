name = input("what is your name?\n ")
othername = input("and what is the other person's name?\n ")

print("hello " + name + " and " + othername)

age = input("how old are you?\n ")
age = int(age)

otherage = input("and how old is the other person?\n ")
otherage = int(otherage)

age_differ = (age)-(otherage)
#age_differ = input(int(age)-int(otherage))
age_differ = abs(age_differ)

print("you are " + str(age_differ) + " years apart.")
