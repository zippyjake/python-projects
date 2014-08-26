Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
What is your name? jake
Who is the other person' name? iqsfdh iawd
How old are you? 11
how old is iqsfdh iawd ? cxvlkxcv
Hi jake and iqsfdh iawd you are 11 years old and cxvlkxcv years old.
>>> ================================ RESTART ================================
>>> 
What is your name? jake
Who is the other person' name? sdfsdf
How old are you? 11
how old is sdfsdf ? DFJ INIWEYFWRF
Hi jake and sdfsdf you are 11 years old and DFJ INIWEYFWRF years old.
>>> ================================ RESTART ================================
>>> 
What is your name? jake
> jake
Who is the other person' name? adscasdc
> asdasd
How old are you? 
>>> ================================ RESTART ================================
>>> 
What is your name? 
>jake
Who is the other person' name? 
>i am crap
How old are you?
> 11
Traceback (most recent call last):
  File "C:/Users/JakeSeeber/Documents/GitHub/python-projects/hd.py", line 5, in <module>
    other_age = input("how old is " , other , " ? \n>")
TypeError: input expected at most 1 arguments, got 3
>>> ================================ RESTART ================================
>>> 
What is your name? 
>jake
Who is the other person' name? 
>CRAP
How old are you? 
> 11
Traceback (most recent call last):
  File "C:/Users/JakeSeeber/Documents/GitHub/python-projects/hd.py", line 5, in <module>
    other_age = input("how old is " , other , " ? \n>")
TypeError: input expected at most 1 arguments, got 3
>>> ================================ RESTART ================================
>>> 
What is your name? 
>jake
Who is the other person' name? 
>CRAP
How old are you? 
> 11
how old is the other person? 
>CRAP
Hi  jake  and  CRAP  you are  11  years old and  CRAP  years old.
>>> ================================ RESTART ================================
>>> 
What is your name? 
>jake
Who is the other person' name? 
>aadaas
How old are you? 
> 11
how old is the other person? 
>12
Traceback (most recent call last):
  File "C:/Users/JakeSeeber/Documents/GitHub/python-projects/hd.py", line 7, in <module>
    age_differ = (age)-(other_age)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> ================================ RESTART ================================
>>> 
What is your name? 
>jake
Who is the other person' name? 
>CRAP
How old are you? 
> 11
how old is the other person? 
>12
Traceback (most recent call last):
  File "C:/Users/JakeSeeber/Documents/GitHub/python-projects/hd.py", line 7, in <module>
    age_differ = str(age)-(other_age)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> ================================ RESTART ================================
>>> 
What is your name? 
>JAKE
Who is the other person' name? 
>cra
How old are you? 
> 11
how old is the other person? 
>12
Traceback (most recent call last):
  File "C:/Users/JakeSeeber/Documents/GitHub/python-projects/hd.py", line 7, in <module>
    age_differ = str(age)(other_age)
TypeError: 'str' object is not callable
>>> ================================ RESTART ================================
>>> 
What is your name? 
>jake
Who is the other person' name? 
>sdf
How old are you? 
> 11
how old is the other person? 
>12
Traceback (most recent call last):
  File "C:/Users/JakeSeeber/Documents/GitHub/python-projects/hd.py", line 8, in <module>
    age_differ = abs(age_differ)
TypeError: bad operand type for abs(): 'str'
>>> ================================ RESTART ================================
>>> 
What is your name? 
>jake\
Who is the other person' name? 
>asdsadasd
How old are you? 
> 11
how old is the other person? 
>12
Traceback (most recent call last):
  File "C:/Users/JakeSeeber/Documents/GitHub/python-projects/hd.py", line 17, in <module>
    print("Hi " , name , " and " , other , " you are " , age_differ , " years apart.")
NameError: name 'age_differ' is not defined
>>> ================================ RESTART ================================
>>> 
What is your name? 
>jake
Who is the other person' name? 
>fgwdfsc
How old are you? 
> 11
how old is the other person? 
>12
Hi  jake  and  fgwdfsc  you are  1  years apart.
>>> ================================ RESTART ================================
>>> 
What is your name? 
>Jake
Who is the other person' name? 
>Crap\
How old are you? 
> 11
H?ow old is the other person? 
>
>>> ================================ RESTART ================================
>>> 
What is your name? 
>Jake
Who is the other person' name? 
>Drake
How old are you? 
> 11
How old is the other person? 
>1
Hi  Jake  and  Drake  you are  10  years apart.
>>> 
