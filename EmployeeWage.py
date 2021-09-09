import random
print("Welcome To Employee Wage Computation Program")

# UC5:- Calculating Wages For Month
randomcheck = random.randint(0,9)
IS_PRESENT = 0
FULL_TIME_HR = 8
PART_TIME_HR = 4
WAGE_PER_HR = 20
MONTHLY_WORKING_DAYS = 20

if  randomcheck%2 == 0 :
	print("Employee Is Full Time Worker")
	print("The Monthly Wage Of Employee is: ",MONTHLY_WORKING_DAYS*WAGE_PER_HR*FULL_TIME_HR)
else:
	print("Employee Is Part Time Worker")
	print("The Monthly Wage Of Employee Is: ",MONTHLY_WORKING_DAYS*WAGE_PER_HR*PART_TIME_HR)