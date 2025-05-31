class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Employee(Person):
    def __init__(self,person,salary):
        super().__init__(person.name, person.age)
        self.person = person
        self.salary = salary

    def display_info(self):
        print("\n -----Employee Information------")
        print(f"Salary: {self.salary}")
        super().display_info()
    def calculate_bonus(self):
        return self.salary*0.1
    


class Manager(Employee):
    def __init__(self,employee,department):
        super().__init__(employee.person, employee.salary)
        self.employee = employee
        self.type = "Manager"
        self.department = department
    
    def calculate_bonus(self):
        return super().calculate_bonus() * 0.2
    

employees = []
name = input("Enter Name: ")
age = int(input("Enter age: "))
salary = float(input("Enter Salary: "))
department = input("Enter Department: ")

person = Person(name, age)
employee = Employee(person, salary)
manager = Manager(employee, department)
employees.append(manager)

for employe in employees: 
    print(employe.person.name)
    print(employe.person.age)
    print(employe.salary)
    print(employe.department)
    


        