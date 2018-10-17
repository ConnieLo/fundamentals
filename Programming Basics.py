import math #brings in any math function that isn't included with python
import datetime

realNumber = 5.5555
print(round(realNumber,2))#rounds the number to 2 dp
print(math.trunc(realNumber))#rounds any real number down to the nearest whole number
multiply = 2*5#all variable names are how to perform each arithmetic function
divide = 2/5
add = 2 + 5
subtract = 2-5
exponentiation = 2**5
square_root = math.sqrt(25)
modulus = 5 % 2#gives the remainder which is 1
div = 5//2#gives the maximum amount of times the whole number goes into the other. this gives 2


string = "Hello World"
len(string) #returns the length of the string
print(string[0:3])#returns the portion of the string within these indexes
print(string.find("Hel"))#determines if "Hel" is contained within string and displays the index of where it starts
print(ord("a"))#prints the ascii number of this character
print(chr(97))#prints the ascii character of this number

int("1")#converts the character "1" into an integer
str(123)#converts the integer 123 to a string
float("123.456")#converts the string into a real number
str(123.456)

print(datetime.date(2016,12,16))

hello = "hi"#sets the string "hi" to the variable identifier hello
bye = input()#sets whatever the user types in to the identifier bye

totalBill = int(input("What is the total of your bill?"))
totalwithTip = totalBill * 1.1
print("Each person owes",str(round(totalwithTip/10,2))+".")
