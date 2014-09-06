
import random

print("Magic 8 Ball ")
while True:

    anwsers = ["Yes","No","Maybe"]

    question = input("Ask me a question: \n")

    anwser = random.choice(anwsers)
    print(anwser)
