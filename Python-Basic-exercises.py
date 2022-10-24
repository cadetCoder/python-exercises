Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
myFunction()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    myFunction()
NameError: name 'myFunction' is not defined
myFunction()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    myFunction()
NameError: name 'myFunction' is not defined

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
myFunction
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    myFunction
NameError: name 'myFunction' is not defined. Did you mean: 'function'?
function
<function function at 0x10fe92170>
myFunction()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myFunction()
NameError: name 'myFunction' is not defined. Did you mean: 'function'?
def function ():
  print("This is my function")

  
myFunction
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    myFunction
NameError: name 'myFunction' is not defined. Did you mean: 'function'?
myFunction()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    myFunction()
NameError: name 'myFunction' is not defined. Did you mean: 'function'?

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
myFunction()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    myFunction()
NameError: name 'myFunction' is not defined. Did you mean: 'function'?

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
myfunction()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    myfunction()
NameError: name 'myfunction' is not defined. Did you mean: 'function'?
myfunction()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    myfunction()
NameError: name 'myfunction' is not defined. Did you mean: 'function'?

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
myfunction ()
This is my function
myfunction()
This is my function

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
This is my function

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
This is my function
This is my function

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
This is my function
This is my function 2
main()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    main()
NameError: name 'main' is not defined. Did you mean: 'min'?

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
main()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    main()
  File "/Users/Darrel/Documents/Python exercises/Python-Basics.py", line 9, in main
    function()
NameError: name 'function' is not defined. Did you mean: 'function1'?

================================ RESTART: Shell ================================
main()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    main()
NameError: name 'main' is not defined. Did you mean: 'min'?

====== RESTART: /Users/Darrel/Documents/Python exercises/Python-Basics.py ======
main()
This is my function
This is my function 2
hello(name)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    hello(name)
NameError: name 'name' is not defined
hello()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    hello()
TypeError: hello() missing 1 required positional argument: 'name'
def hello('Jess'):
    
SyntaxError: invalid syntax
def hello('Jess'):
    
SyntaxError: invalid syntax
def hello("Jess"):print("Hello")
SyntaxError: invalid syntax
def hello("Jess"):
  print("Hello")
  
SyntaxError: invalid syntax
name="Boss"
def hello("name"):
  print("Hello")
  
SyntaxError: invalid syntax

================================ RESTART: Shell ================================
def hello(name):
    print("Hello", name,"!")

    
hello("Jess")
Hello Jess !
name="Joe"
hello(name)
Hello Joe !
name=str("Joe")
hello(name)
Hello Joe !
name=str("Star")
hello(name)
Hello Star !
mynewfunction(4)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    mynewfunction(4)
NameError: name 'mynewfunction' is not defined
You pass me:
    
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax

clear()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
mynewfunction(4)
you passed me:
    
SyntaxError: multiple statements found while compiling a single statement
def mynewfunction(4)
you passed me:
    
SyntaxError: invalid syntax
mynewfunction()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    mynewfunction()
NameError: name 'mynewfunction' is not defined
newfunction(4)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    newfunction(4)
NameError: name 'newfunction' is not defined
mynewfunction(4)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    mynewfunction(4)
NameError: name 'mynewfunction' is not defined
def mynewfunction(4)
  print("you passed me:\t")
  
SyntaxError: invalid syntax
def mynewfunction(4)
  print("you passed me:\t")
  print(4)
  
SyntaxError: invalid syntax
def mynewfunction(4):
  print("you passed me:\t")
  print(4)
  
SyntaxError: invalid syntax
a=300
def mynewfunction("Thanks"):
    
SyntaxError: invalid syntax
def mynewfuntion(X):
    print("You passed me:\t")
    print(X)

    
mynewfunction(20)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    mynewfunction(20)
NameError: name 'mynewfunction' is not defined. Did you mean: 'mynewfuntion'?
mynewfunction(3)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    mynewfunction(3)
NameError: name 'mynewfunction' is not defined. Did you mean: 'mynewfuntion'?
mynewfunction(X):
    
SyntaxError: invalid syntax
mynewfunction(4):
    
SyntaxError: invalid syntax


def mynewfunction(4):
    
SyntaxError: invalid syntax
def mynewfunction(X):
    print("You passed me:\t")
    print(X)

    
mynewfunction(3)
You passed me:	
3
mynewfunction(200)
You passed me:	
200
mynewfunction("Is this new function??")
You passed me:	
Is this new function??
number=400
mynewfunction(number)
You passed me:	
400
myuniversity="Central Bedfordshire University"
mynewfunction(myuniversity)
You passed me:	
Central Bedfordshire University
a=('Test')
mynewfunction(a)
You passed me:	
Test
def Sum3Nums(X,Y,Z):
    answer=X+Y+Z
    print("The answer is"+str(answer))

    
Sum3Nums(5,7,9)
The answer is21
def Sum3Nums(X,Y,Z):
    answer=X+Y+Z
    print("The answer is:\t",+,str(answer))
    
SyntaxError: invalid syntax
def Sum3Nums(X,Y,Z):
    answer=X+Y+Z
    print("The answer is:\t",+str(answer))

    
Sum3Nums(5,6,7)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    Sum3Nums(5,6,7)
  File "<pyshell#86>", line 3, in Sum3Nums
    print("The answer is:\t",+str(answer))
TypeError: bad operand type for unary +: 'str'
def Sum3Nums(X,Y,Z):
    answer=X+Y+Z
    print("The answers is:\t"+str(answer))

    
Sum3Nums(5,6,7)
The answers is:	18
Sum3Nums("my ","dog","Joe")
The answers is:	my dogJoe
>>> Sum3Nums("my ","dog"," Joe")
The answers is:	my dog Joe
>>> def FruitfulSum3Nums(X+Y+Z):
...     
SyntaxError: invalid syntax
>>> def FruitfulSum3Nums(X,Y,Z):
...     answer=X+Y+Z
...     return "The answer is "+str(answer)
... 
>>> result=FruitfulSum3Nums(3,5,6)
>>> result
'The answer is 14'
>>> def ReturnLargest(X,Y):
...     if(X>Y):
...         answer=X
...     else:
...         answer=Y
...     return answer
... 
>>> myresult=ReturnLargest(99,22)
>>> myresult
99
>>> 
>>> def multipleOf3(X):
...     if((X%3)==0):
...         answer=True
...     else:
...         answer=False
...     return answer
... 
>>> result=multipleOf3(21)
>>> result
True
>>> 
... 
>>> def WhereIs(X):
...     if (X=='London'):
...         print('Great Britain')
...     elif(X=='Paris'):
...         print('France')
...     else:
...         print("Sorry, cant't help")
... 
...         
>>> WhereIs('London')
Great Britain
>>> WhereIs('Liverpool')
Sorry, cant't help
