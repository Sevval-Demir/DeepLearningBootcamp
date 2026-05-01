print("="*60)
print("Section 7 : Final")
print("="*60)

from typing import final

class BaseGame:
    def start(self):
        print("Game Started")

    @final #amacı override ettirmemek
    def calculate_score(self,points:int) -> int:
        bonus = 100
        return bonus+points

    def end(self):
        print("Game Ended")

class MyGame(BaseGame):

    def start(self):
        #override
        print("My Game Started")

# sınıf inherite edilmeyecek
@final
class SecretAlgorith:
    def process(self):
        print("secret algorithm used in game")

game = MyGame()
game.start()

