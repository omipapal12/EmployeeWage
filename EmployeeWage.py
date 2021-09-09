import random
print("Welcome To Employee Wage Computation Program")

# UC4:- Solving using Switch Case Statement
randomcheck = random.randint(0, 9)
IS_PRESENT = 1
PART_TIME_HR = 4
FULL_TIME_HR = 8
WAGE_PER_HR = 20


def isPresentOrAbsent():
    return "Employee Is Present"  if randomcheck % 2 == 1 else "Employee Is Absent"


def isPartTime():
    return "Employee Part Time Wage Is:" +str(PART_TIME_HR * WAGE_PER_HR)


def isFullTime():
    return "Employee Full Time Wage Is:" +str(FULL_TIME_HR * WAGE_PER_HR)


def default():
    return "Incorrect Choice"


switcher = {
    1: isPresentOrAbsent,
    2: isPartTime,
    3: isFullTime
}


def switch(employeewage):
    return switcher.get(employeewage, default)()


print(switch(1))
print(switch(2))
print(switch(3))
