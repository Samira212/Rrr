class Shape:
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    def get_info(self):
        return f" Узундугу: {self.a}, Туурасы: {self.b}"
    
    def perimetr (self):
        pass
    def sq (self):
        pass
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def perimetr (self):
        return self.a + self.b + self.c
    
class Tikort(Shape):
 def perimetr (self):
  return (self.a + self.b) * 2
    
triangle1 = Triangle (5, 63, 44)
tik = Tikort (5, 6)
     
print(tik.perimetr())