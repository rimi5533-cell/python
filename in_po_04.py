class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def get_info(self):
        return "브랜드: " + self.brand + ", 가격: " + str(self.price) + "만원"

class Laptop(Computer):
    def __init__(self, brand, price, weight):
        Computer.__init__(self, brand, price)
        self.weight = weight
    def get_info(self):
        return "브랜드: " + self.brand + ", 가격: " + str(self.price) + "만원, 무게: " + str(self.weight) + "kg"

com = Computer("삼성", 120)
lap = Laptop("LG", 150, 1.5)
print(com.get_info())
print(lap.get_info())
