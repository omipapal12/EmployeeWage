import random

print("Welcome To Employee Wage Computation Program")

# UC10:- Employee Wage For Multiple Company Using Constructor

is_absent = 0
is_present_full_day = 1
is_present_part_time = 2
full_day_hours = 8
part_time_hours = 4

class EmpWage():
    def __init__(self,wage_per_hour,number_of_working_days,work_hrs_per_month,company):
        self.wage_per_hour = wage_per_hour
        self.number_of_working_days = number_of_working_days
        self.work_hrs_per_month = work_hrs_per_month
        self.company = company

    def set_total_wage(self,total_wage):
        self.total_wage = total_wage

    def __str__(self) -> str:
        return f"Company = {self.company},Total Emp Wage = {self.total_wage}"

class  EmployeeWage():
    def __init__(self):
        self.company_array = []

    def add_employee(self,wage_per_hour,number_of_working_days,work_hrs_per_month,company):
        self.company_array.append(EmpWage(wage_per_hour,number_of_working_days,work_hrs_per_month,company))

    @staticmethod
    def calculate_daily_wage(wage_per_hour,emp_hrs):
        return emp_hrs * wage_per_hour

    @staticmethod
    def check_emp_working_hours(check_emp):
        emp_attendence = {
            is_present_full_day : full_day_hours,
            is_present_part_time: part_time_hours,
            is_absent: 0
            }
        return emp_attendence.get(check_emp)

    def calculate_employee_salary(self, employee):
        working_days = 0
        total_working_hours = 0
        total_wage = 0
        while (working_days < employee.number_of_working_days and total_working_hours < employee.work_hrs_per_month):
            check_emp = random.randint(0, 2)
            emp_hrs = EmployeeWage.check_emp_working_hours(check_emp)
            total_working_hours = total_working_hours + emp_hrs
            working_days = working_days + 1
            total_wage += self.calculate_daily_wage(emp_hrs, employee.wage_per_hour)
        return total_wage


    def calculate_employee_wage(self):
        for employee in self.company_array:
            total_wage = self.calculate_employee_salary(employee)
            EmpWage.set_total_wage(employee, total_wage)


if __name__ == "__main__":
    print("Welcome to Employee Wage Builder")
    emp_wage = EmployeeWage()
    emp_wage.add_employee(20, 20, 100, "Accenture")
    emp_wage.add_employee(30, 25, 110, "DeepCompute")
    emp_wage.calculate_employee_wage()
    employees = "\n".join(str(employee) for employee in emp_wage.company_array)
    print(employees)
