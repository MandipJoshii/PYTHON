employee_workingTime = ["22","23.9","55","20","90","19","15"]

employee_name = ["dip","mandip","dikshit","kritu","pandey","x","y"]


for i, emp_wt in enumerate(employee_workingTime, start = 0):
    emp_wt = float(emp_wt)
    if emp_wt >= 20:
        print(f"{employee_name[i]} got the bonus because working time = {emp_wt} is greater than 20 \n")
        
    else:
        print(f"{employee_name[i]} didnt got the bonus because woking time =  {emp_wt} is less than 20 \n")    