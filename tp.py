class Animal:
    def make_sound(self):
        pass
class Dog (Animal):
    def make_sound(self):
        return "Гаф гаф"
class Cat (Animal):
    def make_sound(self):
        return "Мияу мияу"
class Bird (Animal):
    def make_sound(self):
        return "Чип чип"
dog = Dog()
cat = Cat ()
bird = Bird ()
print(dog.make_sound())
print(cat.make_sound())
print(bird.make_sound())




