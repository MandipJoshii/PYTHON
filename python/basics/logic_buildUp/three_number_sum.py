#find the sum of 3 numbers


num = int(input("enter a number \n"))

#234 % 10 -> 4
a = num%10


num = num//10

#23 % 10-> 3
b = num%10

num = num//10

#3 % 10 -> 3
c = num%10

print(a+b+c) #4+3+2 = 9
