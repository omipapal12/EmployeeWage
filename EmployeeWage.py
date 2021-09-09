import random
print("Welcome To Employee Wage Computation Program")

# UC2:- Calculate Daily Employee Wage
randomcheck = random.randint(0,9)
IS_PRESENT = 1
IS_ABSENT = 0
FULL_DAY_HR = 8
WAGE_PER_HR = 20
if randomcheck%2 == 1 :
	print("Employee Is Present")
	print("Daily Employee Wage Is:" ,FULL_DAY_HR*WAGE_PER_HR)
else :
	print("Employee Is Absent So There Will be No Any Wage")
