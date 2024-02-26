import random

class Terning():

    def __init__(self, sider):
        self.holdt = False
        self.sider = sider
        self.historik = []
        self.rul()

    # Returnerer  det seneste slag
    def senesteSlag(self):
        return self.historik[len(self.historik)-1]

    # Slaar med terningen og tilfoejer til terningens historik.
    # Returnerer det nye slag
    def rul(self):
        if not self.holdt:
            self.historik.append(random.randint(1, self.sider))
        return self.senesteSlag()

    def hold(self):
        self.holdt = True

    def frigiv(self):
        self.holdt = False

    # Custom implementation af '=='
    def __eq__(self, other):
        return self.senesteSlag() == other.senesteSlag()

    # Custom implementation af '<'
    def __lt__(self, other):
        return self.senesteSlag() < other.senesteSlag()

    def __repr__(self):
        return self.senesteSlag()

    def __str__(self):
        return str(self.senesteSlag())

class Raflebæger():

    def __init__(self):
        self.terninger = []
    def tilføj_terning(self, sider):
        self.terninger.append(Terning(sider))

    def rul(self):
        terningtotal = 0
        for terning in self.terninger:
            terningtal = terning.rul()
            print("d" + str(terning.sider) + ":", terningtal)
            terningtotal += terningtal
        print("Total:  " + str(terningtotal))

class Brik():

    def __init__(self,værdi):
        self.shut = False
        self.værdi = int(værdi)

    def flip(self):
        self.shut = True

class Bræt():
    def __init__(self, size):
        self.brikker = {}
        for i in range(1,size+1,1):
            self.brikker[i] = Brik(i)
        print(self.brikker)
        self.raflebæger = Raflebæger()
        self.raflebæger.tilføj_terning(6)
        self.raflebæger.tilføj_terning(6)
        self.raflebæger.rul()

if __name__ == "__main__":
    r = Raflebæger()
    r.tilføj_terning(10)
    r.tilføj_terning(19)
    r.tilføj_terning(2)
    r.rul()