import random
print("Welcome To Employee Wage Computation Program")

# UC6:- Calculate Wages till a condition of total working hours or days is reached for a month
# Assume 100 hours and 20 days
randomcheck = random.randint(0,9)
IS_PRESENT = 0
FULL_TIME_HR = 8
PART_TIME_HR = 4
WAGE_PER_HR = 20
MONTHLY_WORKING_DAYS = 20
WORKING_HR = 100

if randomcheck%2 == 0 and (WORKING_HR == 100 or MONTHLY_WORKING_DAYS):
    print("Monthly Wage Is : " ,FULL_TIME_HR*WAGE_PER_HR*MONTHLY_WORKING_DAYS)
else :
    print("Part Time Wage:" ,PART_TIME_HR*WAGE_PER_HR*MONTHLY_WORKING_DAYS)
