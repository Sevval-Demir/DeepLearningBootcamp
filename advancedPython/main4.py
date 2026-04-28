# Section 4 : CLASS METHOD
#class metot kullanılırsa self sınıfın kendisine referans verilir

print("="*60)
print("SECTION 4 : class method")
print("="*60)

#alternative constructor

class Pizza:

    total_pizzas = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.total_pizzas +=1 #her obje oluştuğunda total_pizzas sayısını 1 arttır

    @classmethod
    def margherita(cls):
        return cls(["peynir","domates","fesleğen"])
    @classmethod
    def pepperoni(cls):
        return cls(["peynir","sucuk","domates"])
    @classmethod
    def get_total_pizzas(cls):
        return cls.total_pizzas

pizza1 = Pizza.margherita()
print(pizza1.ingredients())
print(Pizza.get_total_pizzas())

