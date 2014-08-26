name = input("What is your name? \n>")
other = input("Who is the other person' name? \n>")

age = input("How old are you? \n> ")
other_age = input("How old is the other person? \n>")

age = int(age)
other_age = int(other_age)

agetotal = abs(age - other_age)

#age_differ = str("(age)(other_age)")
#age_differ = abs(age_differ)

#day_apart = 365.242 * age_differ

print("Hi " , name , " and " , other , " you are " , agetotal , " years apart.")
