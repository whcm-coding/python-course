class Shop(list):
    name = ''
    date = ''

    def __init__(self, clothes):
        self.name = clothes[0]
        self.date = clothes[1]
        self.extend(clothes[2:])

    def cheapest3(self):
        unique_clothes = set(self)

        sorted_unique_clothes = sorted(unique_clothes)
        return sorted_unique_clothes[0:3]

    def add_price(self, the_price):
        self.append(the_price)


with open('clothes.txt',  encoding="utf-8") as clothes:
    data = clothes.readline()
    clothes = data.strip().split(',')
    shop = Shop(clothes)
    print(shop.cheapest3())

    shop.add_price('12')
    print(shop.cheapest3())
