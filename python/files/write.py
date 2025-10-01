import os

print(os.getcwd())

file = open(r"write_file.txt","w")

file.write("hello \n")
file.write("hello \n")


file.close()


