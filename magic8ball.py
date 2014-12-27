import random
anwsers = [
    "Yes",
    "No",
    "Maybe"
]

while True:    
    print("What is your question? ")

    question = input('> ')

    anwser = random.choice(anwsers)
    print(anwser)
