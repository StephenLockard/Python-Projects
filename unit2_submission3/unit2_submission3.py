class Employee:
    def __init__(self, employee_name, employee_id):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.salary = None

    def calculate_salary(self):
        raise NotImplementedError()


class Hourly(Employee):
    def __init__(self, employee_name, employee_id):
        Employee.__init__(self, employee_name, employee_id)
        self.hours_worked = None
        self.pay_rate = None

    def calculate_salary(self):
        self.hours_worked = input("How many hours does the person work each week?")
        self.pay_rate = input("Pay rate:")
        self.salary = int(self.hours_worked) * float(self.pay_rate) * 52


class Yearly(Employee):
    def __init__(self, employee_name, employee_id):
        Employee.__init__(self, employee_name, employee_id)
        self.years = None
        self.basePay = None

    def calculate_salary(self):
        self.years = input("How many years did the employee work at this company?")
        self.basePay = input("The base pay:")
        self.salary = int(self.basePay)+(int(self.basePay)*.10*int(self.years))


employees = list()
employees.append(Hourly("Jim", 1705))
employees.append(Yearly("George", 2213))
for employee in employees:
    employee.calculate_salary()
    print(employee.employee_name, "has salary of", employee.salary, "each year.")
