# what to do in the project
# 1.	Create a (50, 5) array of random marks (0–100).

# 2.	Find average marks per student and per subject.

# 3.	Find highest and lowest scoring student.

# 4.	Find pass/fail count per subject.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
marks = np.random.randint(1,101, size = (10,5))

total = marks.sum()
print("TOTAL SUM OF ALL THE STUDENT SUBJECT MARKS = ", total)

total_marks_student = marks.sum(axis = 1)

print(F"DATA REPRESENTS EACH SUBJECT OF STUDENT MARKS = \n {marks}")

average_student_mark = marks.mean()

print(f"\n DATA REPRESENTS AVERAGE MARKS OF STUDENT = {average_student_mark} \n")

highest_marks = marks.max()
lowest_marks = marks.min()

print(f"STUDENT WITH LARGEST MARKS = {highest_marks} \n")
print(f"STUDENT WITH LOWEST MARKS = {lowest_marks} \n")

#chart -> bar = for finding average marks of students

subjects = np.array(["Maths","Account","Science","Nepali","English"])
plt.bar(subjects,average_student_mark,color="orange")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Students Average Obtained Marks")
plt.show()




passing_marks = 45
def pass_or_fail(marks, passing_marks):
    for i, result in enumerate(marks, start = 1):
        if np.all(result >= passing_marks):
            print(f"STUDENT {i}: PASS \n")
        else:
            print(f"STUDENT {i}: FAIL \n")
        
print(pass_or_fail(marks,passing_marks))

for i, marks in enumerate(total_marks_student, start = 1):
    print(f" {i} Student Total Marks = {marks}")
    
 
 #chart -> bar = to represent pass and fail
passing_score = (marks >= passing_marks).sum(axis=0)
failing_score = (marks < passing_marks).sum(axis=0)
plt.bar(subjects,passing_score,color="green")
plt.bar(subjects,failing_score,bottom = passing_score, label = "fail",color="red")
plt.xlabel("SUBJECT")
plt.ylabel("STUDENTS")
plt.title("PASSING AND FAILING RATIO")
plt.show()
   
    