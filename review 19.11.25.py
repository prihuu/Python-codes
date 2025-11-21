class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def print_info(self):
        print("Food:", self.name)
        print("Calories:", self.calories)

class Fruit(Food):
    def __init__(self, name, calories, is_sweet):
        super().__init__(name, calories)
        self.is_sweet = is_sweet

    def print_info(self):
        super().print_info()
        print(f"Is it sweet?: {"Yes" if self.is_sweet else "No"}")

class Vegetable(Food):
    def __init__(self, name, calories, is_leafy):
        super().__init__(name, calories)
        self.is_leafy = is_leafy

    def print_info(self):
        super().print_info()
        print(f"Is it leafy?: {"Yes" if self.is_leafy else "No"}")

class Store:
    def __init__(self):
        self.inventory = {}

    def add_product(self, food):
        self.inventory[food.name.lower()] = food

    def show_product(self):
        print("Inventory:")
        for food in self.inventory.values():
            food.print_info()

    def buy_product(self, product_name):
        name = product_name.lower()
        if name in self.inventory:
            return self.inventory[name]
        else:
            return None

class Smoothie:
    def __init__(self, name: object, ingredients):
        self.name = name
        self.ingredients = ingredients

        total = 0
        for item in ingredients:
            total += item.calories
        self.total_calories = total

    def smoothie_info(self):
        print("Total calories:", self.name)
        print("Total ingredients:")
        for item in self.ingredients:
            print(item.name)
        print("Total calories:", self.total_calories)

Lidl = Store()

mango = Fruit("Mango", 20, True)
paprika = Vegetable("Paprika", 26, False)
plum = Fruit("Plum", 30, True)
onion = Vegetable("Onion", 40, False)
pineapple = Fruit("Pineapple", 45, True)

Lidl.add_product(mango)
Lidl.add_product(plum)
Lidl.add_product(onion)
Lidl.add_product(pineapple)

Lidl.show_product()

ingredients = []
print("Warmest welcome to Lidl! We have a wide variety of fruits and vegetables. What would you like in your smoothie?:")

while True:
    i = input("Add an ingredient")
    if i.lower() == "":
        break

    product = Lidl.buy_product(i)
    if product:
        ingredients.append(product)
        print(f"I added {product.name} ")
    else:
        print(f"Not available {product.name}")

    if len(ingredients) == 0:
        print("No ingredients added.")

if ingredients:
    name = input("What smoothie is it?: ")
    smoothie = Smoothie(name, ingredients)
    smoothie.smoothie_info()
else:
    print("Smoothie not available.")