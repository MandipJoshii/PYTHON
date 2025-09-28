print("SELECT A NUMBER FROM (1-)")
project = int(input("CHOOSE A PROJECT "))


while True:
 print("0: EXIT")
 if project == 1:
  print("BASIC OF LOOPS")
  for i in range(1,10):
   print(i)
        
 elif project == 2:
  print("BASIC LOOP USING WHILE")  
 i = 0
 while i >= 10:
  print(i)
  i+1
  
 elif project == 0:
 print("EXITING PROGRAM")
 break