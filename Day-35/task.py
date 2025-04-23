class Laptop():
    def __init__(self,brand,display,processor,ram,storage,battery):
        self.brand = brand
        self.display = display
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.battery = battery

    def about(self):
        return f"This is {self.brand} laptop with features such as {self.display}, {self.processor}, {self.ram}, {self.storage}, {self.battery}."
    

laptop1 = Laptop("hp","14 inch","intel i5","8gb","512gb","65whr")
laptop2 = Laptop("asus","15.6 inch","intel i7","16gb","512gb","75whr")
laptop3 = Laptop("dell","14 inch","intel i5","16gb","512gb","65whr")
laptop4 = Laptop("apple","14 inch","M1","8gb","512gb","55whr")

print(laptop1.about())
print(laptop2.about())
print(laptop3.about())
print(laptop4.about())

        