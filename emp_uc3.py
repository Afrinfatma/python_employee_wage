import random

class Employee_wage:

    def calculate_emp_wage(self):
        emp_check=random.randint(0,2)
        wage_per_hr = 20
        if emp_check == 1:
            print("Employee is present")
            daily_emp_wage = wage_per_hr * 8
            print ("Daily wage of employee as full time is:" ,daily_emp_wage)
        elif emp_check == 2:
            print("Employee is present")
            daily_emp_wage = wage_per_hr * 4
            print("Daily of wage of the employee as part time :",daily_emp_wage)
        else:
                print("Employee is absent")
if __name__=='__main__':
    emp=Employee_wage()
    emp.calculate_emp_wage()
