class Computer:
    def __init__(self, RAM, CPU, storage):
        self.RAM = RAM
        self.CPU = CPU
        self.storage = storage

    def get_info (self):
        return f"память: {self.RAM}, процессор: {self.CPU}"

class Laptop(Computer):
    def __init__(self, RAM, CPU, storage, price):
        super().__init__(RAM, CPU, storage)
        self.price = price
    
    def get_info(self):
        return f"память: {self.RAM}, процессор: {self.CPU}, цена: {self.price}"
    
    def get_total (self):
       return self.price 

class Desktop (Computer):
    def __init__(self, RAM, CPU, storage, Model):
        super().__init__(RAM, CPU, storage)
        self.Model = Model

    def get_info (self):
        if self.Model ==  "gygate":
            return "Cool"
        else: 
            return "Not cool"
        
computer1 = Computer (256, "Intel i5")
laptop1 = Laptop (256, "Ryzen 5", 70000)
desktop1 = Desktop ( ) 
print(computer1.get_info())
print(laptop1.get_info())
print(desktop1.get_info())

    
