name = input("what is your name?\n ").strip().title()
othername = input("and what is the other person's name?\n ").strip().title()

print("hello " + name + " and " + othername)

age = input("how old are you " + name + " ?\n" .format(name)).strip()
age = int(age)

otherage = input("and how old is " + othername + " ?\n".format(name)).strip()
otherage = int(otherage)

age_differ = (age)-(otherage)
#age_differ = input(int(age)-int(otherage))
age_differ = abs(age_differ)

day_apart = 365.242 * age_differ


print("you are " + str(age_differ) + " years apart and " + str(day_apart) + " days apart.")
#print("you are " + str(age_differ) + " years apart and " + day_apart + " days apart.")
