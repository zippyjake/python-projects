def question1():
    print('''
    What is 7*3? 
    ''')

    anwser = input('> ')
    
    if anwser == '21':
        print("Correct")
        return True
    else:
        print("Nope")
        return False

def question2():
    print('''
    Who is the hero in the Legend of Zelda? 
    ''')

    anwser = input('> ')
    
    if anwser == 'Link':
        print("Correct")
        return True
    else:
        print("Nope")
        return False

def question3():
    print('''
    What was Nintendo's first system?
    ''')

    anwser = input('> ')
    
    if anwser == 'NES':
        print("Correct")
        return True
    else:
        print("Nope")
        return False
    
questions = [
    question1,
    question2,
    question3

]

import random

while questions:
    question = random.choice(questions)
    correct = question()
    if correct:
        questions.remove(question)
