class employee():
    company = "hp"
    def __init__(self, name,  salary):
        self.name = name
        self.salary = salary
    
    #instance method 
    def get_info(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
    
    #static method
    @staticmethod
    def multi(a, b):
        return a*b
    
    #class method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


ep1 = employee("nilesh",2000)
ep1.get_info()
print(ep1.multi(2,3))
print(employee.company)
ep1.change_company("hitachi")
print(employee.company)

        
    
