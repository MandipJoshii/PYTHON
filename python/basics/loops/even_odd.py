number = int(input("enter the number "))



for num in range(1,number):
    if num % 2 == 0:
     print(f"even = {num}")
    else:
     print(f"odd = {num}")