# SECTION 1 : DECORATORS
#decoratorlar tekrarı önlüyor

print("="*60)
print("SECTION 1 : DECORATORS")
print("="*60)

def my_decorator(func):

    def wrapper():
        print("wrapper function executed")
        func()
        print("wrapper function executed")
    return wrapper #fonksiyonun kendisi döndürülüyor

@my_decorator
def hello_world():
    print("Hello World")

hello_world()