import random
class Employee_wage:
        def calculate_emp_wage(self):
                emp_check = random.randint(0, 1)
                is_present = 1
                wage_per_hr = 20
                full_day_hr = 8
                if emp_check == is_present:
                        print("Employee is present")
                        daily_emp_wage = wage_per_hr * full_day_hr
                        print("Daily of wage of the employee is :", daily_emp_wage)
                else:
                        print("Employee is absent")
if __name__=='__main__':
       emp=Employee_wage()
       emp.calculate_emp_wage()