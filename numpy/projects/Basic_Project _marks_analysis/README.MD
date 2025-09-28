LEARN WHILE CODING:


1: FIRST CONCEPT -> np.random.seed(0)

to generate same number everytime we try to generate a random number

FOR EXAMPLE:
IN THIS CODE 

import numpy as np

np.random.seed(0) 
marks = np.random.randint(1,101, size=(10,5))

print(marks)

EVERYTIME WE RUN THE PROGRAM WE WILL GET SAME RANDOM NUMBER.
WHICH IS:
 [ 45  48  65  68  68]
 [ 10  84  22  37  88]
 [ 71  89  89  13  59]
 [ 66  40  88  47  89]
 [ 82  38  26  78  73]
 [ 10  21  81  70  80]
 [ 48  65  83 100  89]
 [ 50  30  20  20  15]
 [ 40  33  66  10  58]
 [ 33  32  75  24  36]


2: SECOND CONCEPT -> np.random.randint(a,b, size = (x,y))
random.randint(1,11) -> generate random number starting from 1 and ending to 10(11 doesnt count)

More Advance USE OF -> random.randint()

random.randint(1,11, size = (50,5))

where (1,11) -> random number we can have ranging from 1 to 10
where size(50,5) -> 50 is rows and 5 is column 

FOR EXAMPLE
size = (10,5)
        c1 c2 c3 c4 c5
row1 = [ 8  4  8  8  9]
row2 = [ 5  9  6  9  5]
row3 = [ 3  2  6  4  5]
row4 = [ 8  1  5  8  8]
row5 = [ 7  0  2  5 10]
row6 = [ 7  1  6  4  3]
row7 = [ 5  0  5  4  0]
row8 = [ 5  2  6  8  2]
row9 = [ 5  6  8  9  4]
row10= [ 5  5 10 10 10]

THE random.randint(1,101, size = (50,5)) -> can be use to generate a random marks out of 100 for 50 students having 5 different subjects 

3: Third Concept -> axis
 a. axis = 1 -> row
 b. axix = 0 -> column