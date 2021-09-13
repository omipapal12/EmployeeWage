import random
from py_compile import main

print("Welcome To Employee Wage Computation Program")

# UC8:- Using Class

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4
TOTAL_WORKING_DAYS = 20
TOTAL_WORKING_HOURS = 100


class Employee:
    def calculate_wage(self):
        emp_attendence = {
            IS_PRESENT_FULL_DAY: FULL_DAY_HOURS,
            IS_PRESENT_PART_TIME: PART_TIME_HOURS,
            IS_ABSENT: 0
        }
        counter = 0
        working_days = 0
        total_working_hours = 0
        while working_days < TOTAL_WORKING_DAYS and total_working_hours < TOTAL_WORKING_HOURS:
            try:
                user_input = int(input("Enter the number for  attendance \n0-For Absent \n1- For Is Present Full Day "
                                       "\n2- For Is Present Part Time \n"))
                total_working_hours = total_working_hours + emp_attendence.get(user_input)
                working_days = working_days + 1
                counter = counter + 1
            except ValueError:
                print("Enter valid input")
            else:
                print(f"total wage of  days  {counter} is =  {WAGE_PER_HOUR * total_working_hours}")

        return WAGE_PER_HOUR * total_working_hours

emp = Employee()

if __name__ == "__main__":
    main()
total_wage = emp.calculate_wage()
print("Employee total wage is ", total_wage)