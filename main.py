
# class Rectangle:
#   """ეს არის Rectangle კლასის დოკუმენტაცია"""
  
#   def __init__(self, lenght, width):
#     self.width=width
#     self.lenght=lenght
#   def perimeter(self):
#     return 2 * (self.width + self.lenght)
#   def area(self):
#     return self.width * self.lenght
# obj1=Rectangle(5,1)
# onj2=Rectangle(3,3)
# obj3=Rectangle(7,3)
# print(obj1.area())


# class Car:
#   def __init__(self,brand,model,colour):
#     self.brand=brand
#     self.model=model
#     self.colour=colour
#   def __str__(self):
#     return f"that {self.brand} {self.model} is {self.colour}"
# car1 = Car('ford','mustang','red')
# car2 = Car('Toyota','prius','blue')
# car3 = Car('Volksvwagen','golf','green')
# print(car1)
# print(car2)
# print(car3)


class Dog:
  def __init__(self,breed,size,age,colour):
    self.breed=breed
    self.size=size
    self.age=age
    self.colour=colour
  def sleep(self):
    return "is sleeping"
  def eat(self):
    return "is sleeping"
  def sit(self):
    return "is sitting"
  def run(self):
    return "is running"
  def __str__(self):
    return f"{self.age} old {self.colour},{self.size} sized,{self.breed}"
dog1 = Dog("neapolitan mastiff","large","7 years","black")
print(dog1,dog1.sleep())
dog2 = Dog("maltese","small","2 years","white")
print(dog2,dog2.run())
dog3 = Dog("CHow Chow","medium","3 years","brown")
print(dog3,dog3.eat())

