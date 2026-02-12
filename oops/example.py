class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

class Developer(Employee):
    def get_salary(self):
        return self._salary + 10000

emp = Developer("Aarush", 50000)
print(emp.get_salary())
