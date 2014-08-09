
def die():
    print("good bye.")
    print("you died")
def live():
    print("fine of you go then.")
    print("you lived")
def ask(question):
    answer = input(question)
    answer = answer.strip().lower()
    print("thou hast anwsered " + answer)
    return answer
def ask_color():
    answer = ask("what is your favorite color?\n ")
    return answer
def ask_capital():
    anwser = ask("what is the capital of Assyria?\n ")
    return answer
def ask_anwser():
    anwser = ask("what is the air speed velocity of an unladen swallow?\n ")
    return answer







##########################################



name = ask("what is your name?\n ")
quest = ask("what is your quest?\n ")

if name == 'lancelot':
    color = ask_color()
    print(color)
    if color == 'blue':
        live()
    else:
        die()
elif name == 'robin':
    capital = ask_capital()
    if capital == 'assur' or capital == 'ashur':
        live()
    else:
        die()
elif name == 'galahad':
    color = ask_color()
    if color == 'blue':
        die()
    else:
        live()
elif name == 'arthur':
    color = ask_anwser()
    if anwser == 'what do you mean, an afercan or european swallow?':
        live()
        print("the bridge keeper died")
    elif anwser == '25 mph':
        live()
    else:
        die()
else:
    color = ask("what is your favorite color?\n ")
    if color != '' :
        live()
    else:
        die()
    
