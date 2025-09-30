"""
int
float/decimal
string
boolean

list(array) -> []
tupils -> ()

dictionary
complex number

"""

print(12)
print(12.5)
print(True)
print(False)
print("lunetic french",1,2.5,True,sep='|',end="o")


list = [12,22,45,"x","21"]
print(list)

tupils = (12,22,34)
print(tupils)

dictionary = {
    "name":"mandip",
    "age":21,
    "salary":21000
}
print(dictionary)

complex = 2+21j
print(complex)

print(type([1,2,3,4,5]))
print(type(2+21j))
print(type({
    "name":"mandip",
    "age":21,
    "salary":21000
}))



"""
VARIABLES:

5-10 MARKS

STATIC BINDING VS DYNAMIC BINDING 




STATIC TYPES VS DYNAMIC TYPES
  1.1 STATIC TYPING
    A. WHERE DATA TYPES NEED TO BE DECLARE BEFORE EXECUTING THEM, AND VARIABLE CANNOT STORE MORE THAN ONE DATA.
    B. IT IS CHECKED AT COMPILE TIME
    C.FOR EXAMPLE
     int age = 21

 1.2 DYNAMIC TYPING
    A. WHERE DATA TYPES DOESN'T NEED TO BE DECLARED AND VARIABLE CAN STORE MORE THAN ONE DATA.
    B. IT IS CHECKED AT RUN-TIME.
    C. FOR EXAMPLE
     name = "mandip"
     name = "x"
     print(name)
     print(name)

BUT WAIT, THERE IS A ONE WAY TO DECLARE VARIABLES STATIC.
 BUT WHY WE NEED TO DO IT, BECAUSE WHILE ADDING 5+5 AND '5'+'5' IT GIVES DIFFERENT OUTPUT SO TO PREVENT IT
 WE CAN YOU TYPE HINTS

 FOR EXAMPLE:
 def add(a:int, b:int)-> int: {
 return a+b
 }  

 print(add(5+5))       
STYLISH DECLARATION TECHNIQUES

"""


def add(a:int, b:int) -> int:
    return a+b

print(add(5,5))
print(add("5","5"))



"""
MULTIPLE VARIABLE CREATION CHEAT CODE

a,b,c = 10,20,30
print(a,b,c)


OR

a=b=c = 5
print(a,b,c,sep=',')
"""