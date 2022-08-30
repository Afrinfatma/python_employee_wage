import random
class Employee_wage:

    def calculate_emp_wage(self):
        part_time = 1
        full_time = 2
        emp_rate_per_hr = 20
        num_of_working_days=20
        total_emp_wage = 0
        emp_hrs=0
        for day in range (num_of_working_days):
            emp_check = random.randint(0, 2)
            if emp_check == 1:
                print("Employee is present as part time")
                emp_hrs= 4

            elif emp_check == 2:
                print("Employee is present as full time")
                emp_hrs= 8

            else:
                    print("Employee is absent")
            emp_wage=emp_rate_per_hr * emp_hrs
            total_emp_wage =total_emp_wage + emp_wage
            print( "Daily wage of the employee:" ,emp_wage)
        print("Total wage of an employee for a month" ,total_emp_wage )


if __name__=='__main__':
    emp=Employee_wage()
    emp.calculate_emp_wage()

