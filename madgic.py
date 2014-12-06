import random

print("Pie")
while True:
    question = input("What is your question? ")
    print(question)
    answers = ['Yes','Maybe','No']
    answer = random.choice(answers)
    print(answer)
