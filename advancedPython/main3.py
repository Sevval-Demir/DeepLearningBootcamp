# section 3 : static method

print("="*60)
print("SECTION 3 : static method")
print("="*60)

class MathOps:

    #static metotlara instance oluşturmadan ulaşılabilir
    @staticmethod
    def add(a,b):
        return a+b

print(MathOps.add(2,3))
