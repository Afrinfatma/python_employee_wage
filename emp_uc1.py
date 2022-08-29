import random

is_present=1

if __name__=='__main__':
        emp_check=random.randint(0,1)
        if emp_check == is_present:
                print("Employee is present")
        else:
                print("Employee is absent")

