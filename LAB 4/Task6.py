from abc import ABC , abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    @abstractmethod
    def calculateBonus(self):
        pass
    def display(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculateBonus(self):
        self.bonus = self.salary*0.2
    def hire(self,candidate):
        print(f"Manager is hiring {candidate}")
    def display(self):
        super().display()
        print(f"The bonus of the manager is {self.bonus}")        
class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculateBonus(self):
        self.bonus = self.salary*0.1
    def writeCode(self):
        print(f"Developer is writing code")
    def display(self):
        super().display()
        print(f"The bonus of the developer is {self.bonus}")
class SeniorManager(Manager):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculateBonus(self):
        self.bonus = self.salary*0.3
    def display(self):
        Employee.display(self)
        print(f"The bonus of the senior manager is {self.bonus}")

manager = Manager("Muhammad Baqar Laghari",200000)
manager.calculateBonus()
manager.hire("Kashif")
manager.display()
developer = Developer("Muhammad Omer Siddiqui",250000)
developer.calculateBonus()
developer.writeCode()
developer.display()
senior_manager = SeniorManager("Syed Anwar Kamal Rizvi",250000)
senior_manager.calculateBonus()
senior_manager.display()