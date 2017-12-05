import datetime

class Employee:
    num_of_emp = 0
    bonus = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

        Employee.num_of_emp += 1

    @property
    def email_address(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return '{},{}'.format(self.last, self.first)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None

    @classmethod
    def raise_bonus(cls, bonus):
        cls.bonus = bonus

    @classmethod
    def from_string(cls,str):
        first, last, salary = str.split('-')
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return 'Employee({} , {}, {} )'.format(self.first, self.last, self.salary)

    def __str__(self):
        return 'Employee - First Name: {}, Last Name: {}, Salary: {}'.format(self.first, self.last, self.salary)

    def __add__(self, other):
        return self.salary + other.salary


if __name__ == '__main__':
    emp_1 = Employee('Suriya', 'Mohan', 5000)
    emp_2 = Employee('Bala', 'G', 6000)

    str = 'karthi-s-7000'

    # alternate constructor
    emp_3 = Employee.from_string(str)


    print(emp_1.full_name())

    print(Employee.num_of_emp)

    dt = datetime.date(2017,11,30)

    print(Employee.is_workday(dt))

    print(emp_2)

    print(emp_1 + emp_2)


