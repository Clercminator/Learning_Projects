class Employee:

    num_of_emp = 0 #class variable
    raise_amount = 1.04 #instance variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    
    
emp1 = Employee('David','Clerc',50000)
emp2 = Employee('Gabriela','Sosa',100000)

emp1.raise_amount = 1.05

print(emp1.fullname())
print(Employee.fullname(emp2))
print(emp1.raise_amount, emp2.raise_amount)
print(Employee.num_of_emp)
