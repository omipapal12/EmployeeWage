import random
print("Welcome To Employee Wage Computation Program")

# UC1:- Check Employee Is Present Or Absent
randomcheck = random.randint(0, 9)
IS_PRESENT = 1
IS_ABSENT = 0
if randomcheck%2 == 1:
	print("Employee Is Present" )
else :
	print("Employee Is Absent")
