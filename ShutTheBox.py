 #Shut the box view group

import GameController

# Number of bricks selector
class ShutTheBox:
    def __init__(self):
        mode = self.intro()
        self.gc = GameController.GameController(mode)

    def intro(self):
        print("Intro")
        while True:
            Option1 = input("How many numbers would you like to play with 9 or 12? ")

            Choice = 0  # This name is temp', but should allow us to use the controller
            # / model given that we can change the name.

            if Option1 == "12":
                Choice = 12  # Sets the choice stat to 12,
                break

            elif Option1 == "9":
                Choice = 9  # Sets the choice stat to 9,
                break

            else:
                print("Please choose either 9 or 12")  # Error handling

        print(Choice, "mode picked.")
        return Choice

    def render(self):
        print('Du har slået:\n{} og {}'.format(self.gc.bræt.raflebæger.terninger[0], self.gc.bræt.raflebæger.terninger[1]))
        out = '|'
        for nummer in self.gc.bræt.brikker:
            brik = self.gc.bræt.brikker[nummer]
            if brik.shut:
                out += ' X |'
            else:
                out += ' {} |'.format(nummer)
        print(out)
    def run(self):
        self.render()
        running = True
        while running:
            # input
            flipList = input('Hvilke brikker skal lukkes?\nAdskil med komma\n').split(',')
            for i in range(len(flipList)):
                flipList[i] = int(flipList[i])
            # update
            succes = self.gc.flip(flipList)
            if not succes:
                print('Du kan ikke flippe den kombination')
            else:
                self.gc.bræt.raflebæger.rul()
            # render
            self.render()


# https://docs.google.com/document/d/1gSRzIXMDmgNAJoKjsw4HnSXA8wjWLx3KdBaUJf6oThw/edit , Intro segment

if __name__ == "__main__":
     game = ShutTheBox()
     game.run()