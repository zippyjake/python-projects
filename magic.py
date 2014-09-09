import random

answers = ["Yes","No","Maybe"]

while True:

    question = input("What is your very important question: \n")

    anwser = random.choice(answers)
    print(anwser)
