def link():
    print("Who is the hero in the Legend of Zelda? ")
    q1 = input('> ')
    if q1 == 'Link':
        print("Correct")
        return True
    else:
        print("False")
        return False

def NES():
    print("What was the first system Nintendo made? ")
    q2 = input('> ')
    if q2 == 'NES':
        print("Correct")
        return True
    else:
        print("False")
        return False
        
def TwentyOne():
    print("What is 7*3? ")
    q3 = input('> ')
    if q3 == '21':
        print("Correct")
        return True
    else:
        print("False")
        return False

questions = [
    link,
    NES,
    TwentyOne
]

import random
while questions:
    question = random.choice(questions)
    correct = question()
    if correct:
        questions.remove(question)
