print("="*60)
print("SECTION 6: OVERLOADING")
print("="*60)

from typing import overload,Union

def example(x:int):
    return x*2

print(example(5))

class Calculator:
    @overload
    def add(self, a:int, b:int) -> int:
        ...

    @overload
    def add(self, a:int, b:int, c:int) -> int:
        ...

    def add(self, a:int, b:int, c:int | None = None) -> int:
        if c is None:
            return a + b
        return a + b + c

    @overload
    def process(self, value:int) -> int:
        ...

    @overload
    def process(self, value:str) -> str:
        ...

    def process(self, value: Union[int,str]) -> Union[int,str]:
        if isinstance(value, int):
            return value * 2
        elif isinstance(value, str):
            return value.upper()
        else:
            raise ValueError("Invalid type")

calculator = Calculator()
print(calculator.add(10, 20))

calculator2 = Calculator()
print(calculator2.add(10, 20, 30))

result = calculator.process("sevval")
print(result)