#Create employee class
class Employee:
#declare attributes
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 
#create a formula to calculate salary increase from percentage.    
    def salary_increase(self, percent_increase):
        return self.salary + self.salary * percent_increase
#create new instance sample    
john_salary = Employee("John", 5000)
#print instance with salary increase.
print("John's salary increased to: ", john_salary.salary_increase(.10))
