class Employee:
    def __init__(self, name, age, salary, emloyment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = emloyment_years

    def get_annual_salary(self,):
        return self.salary * 12
    
    def __str__(self):
         return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}"

employee1 = Employee("Khaled", 26, 100, 4)

# print(employee1.get_annual_salary())      #Testing




class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
         return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}, Bonus: {int(self.get_bonus())}"

manager1 = Manager("Khaledd", 26, 200, 4, 0.1)
print(manager1)     #testing


'''
def main():
	# main code here

if __name__ == '__main__':
	main()
'''