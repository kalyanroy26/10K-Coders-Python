#class1
class bird():
    fly = True

eagle = bird()

print(eagle.fly)

#class 2
class vehicle():
    wheels = 0
    brand = ''
    def gears(self):
        return "6 gears"
    
truimph = vehicle()
truimph.wheels = 2
print(truimph.wheels)
print(truimph.gears())

#class3
class animal():
    legs = 0
    sound =''
    walk = True

dog = animal()
dog.legs = 4
dog.sound = 'bark'
print(dog.legs)
print(dog.sound)