#!/usr/bin/python

class Employee:
   empCount = 0

   def __init__(self, name, salary, age):
      self.name = name
      self.salary = salary
      self.age = age
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary, ", Age: ", self.age)

emp1 = Employee("Zara", 2000, 45)
emp2 = Employee("Manni", 5000, 32)
emp3 = Employee("Ram", 4500, 56)    

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
