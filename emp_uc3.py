import random


class Employeewage:
    def __init__(self):
        self.part_time = 1
        self.full_time = 2

    def compute_emp_wage(self, company, emp_rate_per_hr, num_of_working_days, max_hrs_per_month):
        total_emp_wage = 0
        emp_hrs = 0
        total_working_days = 0
        total_working_hrs = 0

        while total_working_hrs <= max_hrs_per_month and total_working_days <= num_of_working_days:
            total_working_days = total_working_days + 1
            emp_check = random.randint(0, 2)

            if emp_check == 1:
                print("Employee is present as part time")
                emp_hrs = 4

            elif emp_check == 2:
                print("Employee is present as full time")
                emp_hrs = 8

            else:
                print("Employee is absent")
            total_working_hrs = total_working_hrs + emp_hrs
            print('day ', total_working_days, "emp hours", emp_hrs)
        total_emp_wage = emp_rate_per_hr * total_working_hrs

        print("Total wage of an employee for a month", total_emp_wage)


if __name__ == '__main__':
    emp = Employeewage()
    emp.compute_emp_wage("Reliance", 20, 20, 100)
