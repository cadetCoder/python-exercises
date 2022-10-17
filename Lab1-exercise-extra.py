#Programming Workshop 1 - Extra Exercises

#P1
print("2¹ = ",2**1)
print("2² = ",2**2)
print("2³ = ",2**3)
print("2⁴ = ",2**4)
print("2⁵ = ",2**5)
print("2⁶ = ",2**6)
print("2⁷ = ",2**7)
print("2⁸ = ",2**8,"\n")

#P2
num = int(input("What power of two?\t")) #The \t escape sequence shown here adds an invisible tab character to format the output.
sum = (2**num)
print ("Two to the power of", num, "is", sum,"\n")

#P3
num = int(input("What case?\t"))
power = int(input("What power of 10?\t"))
sum = (num**power)
print(num,"to the power of", power, "is", sum, "\n")


#P4
num_digits = 4
value = 0
err = False
for i in range (num_digits):
    if i==0:
        n = int(input("Enter leftmost digit:\t"))
    else:
        n = int(input("Enter the next digit:\t"))
    if n==0:
        pass
    elif n==1:
        power = (num_digits-1)-i
        value += (int)(pow(2, power))
    else:
        err = True
        break
if err:
    print("Error! Incorrect binary number.")
else:
    print("The value is", value, "\n")

#P5
import math
city = int(input("How many cities?\t"))
routes = math.factorial(city)
print("For", city, "cities, there are", routes, "possible routes\n")

#P6
name = input("What is your first name?\t")
surname = input("what is your lastname?\t")
print("Hello", name, surname, "\n")
print("Welcome to Python", end = "!")
