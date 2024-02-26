 #Shut the box view group

import GameController

# Number of bricks selector
class ShutTheBox:
    def __init__(self):
        print("Innit")

    def GameController(GC):
        print("GC")

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

 # https://docs.google.com/document/d/1gSRzIXMDmgNAJoKjsw4HnSXA8wjWLx3KdBaUJf6oThw/edit , Intro segment