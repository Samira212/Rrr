class Car :
    def __init__(self, brand, nomer, model):
        self.brand = brand
        self.nomer = nomer
        self.model = model
         
    def get_info (self):
        return self.brand, self.nomer, self.model
    
car1 = Car  ("Audi", "01KG 657 ASW", "RS7")
car2 = Car ("Mercedes", "08KG 786 LKJ", "S")

print(car1.get_info())
