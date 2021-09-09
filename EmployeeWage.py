import random
print("Welcome To Employee Wage Computation Program")

#UC3:- Add Part Time Employee & Wage
randomcheck = random.randint(0,9)
IS_PART_TIME = 1
IS_FULL_TIME = 2
FULL_DAY_HR = 8
PART_TIME_HR = 4
WAGE_PER_HR = 20
if randomcheck%2 == 1:
	print("Employee Is Part Time")
	print("So Employee Daily Part Time Wage Is: " ,PART_TIME_HR*WAGE_PER_HR)
else:
	print("Employee Is Full Time")
	print("So Employee Daily Full Wage Is: " ,FULL_DAY_HR*WAGE_PER_HR)

