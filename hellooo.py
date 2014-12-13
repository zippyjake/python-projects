print("Hello World")

name = input("What is your name? ")

print("Hello",name)

def pie():
    print('''
    Is Pie Awesome? 
    ''')

    answer = input('> ')

    if answer == 'yes':
        print("You Have Made the Right Choice")
    else:
        print("...")

def favcolor():
    print('''
    What is your fav color? 
    ''')

    answer = input('> ')

    if answer == 'red':
        print('Correct')
    elif answer == 'orange':
        print('Correct')
    elif answer == 'yellow':
        print('Correct')
    elif answer == 'green':
        print('Correct')
    elif answer == 'blue':
        print('Correct')
    elif answer == 'purple':
        print('Correct')
    elif answer == 'pink':
        print('Correct')
    elif answer == 'black':
        print('Correct')
    elif answer == 'white':
        print('Correct')
    elif answer == 'indigo':
        print('Correct')
    elif answer == 'violet':
        print('Correct')
    elif answer == 'aqua':
        print('Correct')
    elif answer == 'gold':
        print('Correct')
    elif answer == 'siver':
        print('Correct')
    elif answer == 'teel':
        print('Correct')
    elif answer == 'megenta':
        print('Correct')
    elif answer == 'gray':
        print('Correct')
    elif answer == 'bronze':
        print('Correct')
    elif answer == 'cyan':
        print('Correct')
    elif answer == 'vinilla':
        print('Correct')
    else:
        print('Incorrect')
questions = [
    favcolor,
    pie
]

import random

while questions:
    question = random.choice(questions)
    correct = question()
    if correct:
        questions.remove(question)
