class Animal:
    def make_sound ():
        pass

class Dog(Animal):
    def make_sound():
        return "Гаф-Гаф!"
    
class Cat(Animal):
    def make_sound():
     return "Мияу-Мияу!"
    
class Bird(Animal):
    def make_sound():
        return "Чип-Чип!"
    
dog = Dog
cat = Cat
bird = Bird

print(dog.make_sound())
print(cat.make_sound())
print(bird.make_sound())
