import random
while True:
    question = input("What is your question? ")

    anwsers = [
        "Yes",
        "Maybe",
        "No"
        ]

    answer = random.choice(anwsers)
    print(answer)
