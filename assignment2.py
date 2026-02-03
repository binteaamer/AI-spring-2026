#task 1
#task 1 
class vehicle:
  def __init__(self,vehicle_id,brand,rent_per_day):
    self.vehicle_id=vehicle_id
    self.brand=brand
    self.rent_per_day=rent_per_day
  
  def display_details(self):
    print("vehicle id is ", self.vehicle_id)
    print(f"vehicle brand is {self.brand}")
    print(f"rent per day is {self.rent_per_day}")

  
  def calculate_rent(self, days):
    return days*self.rent_per_day


v1 = vehicle(123,"toyota",14)
v2 = vehicle(124,"suzuki",15)
v1.display_details()
v2.display_details()

days=int(input("enter the days"))
rent=v1.calculate_rent(days)
print(f"total rent is {rent}")
rent=v2.calculate_rent(days)
print(f"total rent is {rent}")

#task 2 
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary
    def calculate_salary(self): 
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):  
        return self.hourly_rate * self.hours_worked

f1 = FullTimeEmployee("Abeeha", 940, 10000)
p1 = PartTimeEmployee("Mannan", 896, 200, 8)
print(f"Full Time Employee {f1.name} Salary:", f1.calculate_salary())
print(f"Part Time Employee {p1.name} Salary:", p1.calculate_salary())

#task 3 

class Student:
  def __init__ (self, name):
      self.name=name
      self.__marks= 0 
   
  def set_marks(self,marks):
    self.__marks=marks
  def get_marks(self):
    return self.__marks

  def calculate_grade(self):
    if self.__marks>=80:
      return "A"
    elif self.__marks>=70:
      return "B"
    elif self.__marks>=60:
      return "C"
    elif self.__marks>=50:
      return "D"
    else:
      return "F"
  
s1=Student ("abeeha")
s1.set_marks(80)

s2= Student("neha")
s2.set_marks(70)

print(s1.name, "- Marks:", s1.get_marks(), "Grade:", s1.calculate_grade())
print(s2.name, "- Marks:", s2.get_marks(), "Grade:", s2.calculate_grade())

