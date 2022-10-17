Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
num1 + num2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    num1 + num2
NameError: name 'num1' is not defined
myName
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    myName
NameError: name 'myName' is not defined
myName = input("Enter name \n")
Enter name 
Darrel
myName
'Darrel'
print("Hello,", myName, "Welcome to the University")
Hello, Darrel Welcome to the University
print("Hello,", myName, ".",ArithmeticError "Welcome to the University")
SyntaxError: invalid syntax
print("Hello,", myName, ".", "Welcome to the University")
Hello, Darrel . Welcome to the University
print("Hello,", + myName + "." + "Welcome to the University")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("Hello,", + myName + "." + "Welcome to the University")
TypeError: bad operand type for unary +: 'str'
print("Hello," + myName + "." + "Welcome to the University")
Hello,Darrel.Welcome to the University
print("Hello," + myName + ".\n" + "Welcome to the University")
Hello,Darrel.
Welcome to the University
print("Hello," + myName + ".")
Hello,Darrel.
print("Welcome to the University")
Welcome to the University
import math
math.factorial(4)
24
num1 = input("Enter the first number")
Enter the first number
1
1
num1 = input("Enter the first number: \n")
Enter the first number: 
12
type(num1)
<class 'str'>
num2 = input ("Enter the second number: \n")
Enter the second number: 
10
num3 = num1 + num2

num3
'1210'
num3 = int(num1) + int(num2)
>>> num5
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    num5
NameError: name 'num5' is not defined. Did you mean: 'num1'?
>>> num3
22
>>> num1 = int(input("Enter first number: \n"))
Enter first number: 
8
>>> type(num1)
<class 'int'>
>>> num2 = int(input("Enter second number: \n"))
Enter second number: 
65
>>> type(num2)
<class 'int'>
>>> num1 + num2
73
>>> num1 - num2
-57
>>> num1 * num2
520
>>> num2 / num1
8.125
>>> num2//num1
8
>>> num1**num2
50216813883093446110686315385661331328818843555712276103168
>>> 1+1
2
>>> 1+1+2
4
>>> 10-6
4
>>> 3*3
9
>>> 3+3*3
12
>>> 3**3
27
>>> (2+1)*3
9
>>> 1+2+3+4+5
15
>>> 1*2*3*4*5
120
>>> 10/2
5.0
>>> 10/3
3.3333333333333335
>>> 5.0*10
50.0
>>> 10.0/3
3.3333333333333335
