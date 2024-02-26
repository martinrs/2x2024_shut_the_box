import random
import Model

toflip =[]

class GameController:
    def __init__(self,size):
        self.score=0
        self.game_running=True
        self.bræt=Model.Bræt(size)

    def flip(self, inputlist):
        allmoveslegal=True
        for e in inputlist:
            if not self.checkMove(e):
                allmoveslegal=False
        if allmoveslegal:
            for e in inputlist:
                self.bræt.brikker[e].flip()
        return allmoveslegal
    def checkMove(self,num):
        if not num in self.bræt.brikker:
            return False
        elif self.bræt.brikker[num].shut:
            return False
        return True

def checkSum():
    sum = 0
    for terning in bræt.Raflebaeger.terninger:
        sum += terning.senesteSlag
