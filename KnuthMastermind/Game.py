from random import randint

class Game:
    def __init__(self):
        self.turns = None
        self.boardSize = 4
        self.tries = 0
        self.answer = self.genAns()

    def genAns(self):
        return [randint(1,9) for _ in range(self.boardSize)]

    def checkAns(self, checkList, printStats = False):

        #Check if value is in the answer
        if(checkList==self.answer):
            if(printStats):
                print("\n\nSolution found!\nMy Proposed Solution: " + str(checkList))
                print("The Answer: " + str(self.answer))
                print("Tries needed: " + str(self.tries))
            return True, (4, 0)

        inSpot = 0
        inList = 0


        valMount = {value:self.answer.count(value) for value in self.answer}
        myMount = {value:0 for value in checkList}

        # check if there is any in position first
        for i in range(len(checkList)):
            if(checkList[i] == self.answer[i]):
                myMount[checkList[i]] += 1
                inSpot+=1
        # then look for those that might be out of position
        for i in range(len(checkList)):
            if checkList[i] != self.answer[i] and checkList[i] in self.answer and myMount[checkList[i]] < valMount[checkList[i]]:
                myMount[checkList[i]] += 1
                inList+=1

        self.tries += 1

        print("You guessed {}\n"
              "There are {} in the right position and\n "
              "there are {} that belong but are not in the right position.\n".format(checkList, inSpot, inList))

        gTup = (inSpot, inList)

        return False, gTup

    def getUserI(self):
        stringAns = []
        while(not stringAns):
            stringAns = input("Input a {} value integer\n::> ".format(str(self.boardSize)))
            if (stringAns.isdigit() and len(stringAns) == self.boardSize ):
                return [int(inte) for inte in stringAns]
            else:
                print("That is not valid input")
                stringAns = []

    def menu(self):
        print("Puzzle someone mentioned")
        userAns = []
        while(userAns != self.answer):
            userAns = self.getUserI()
            self.checkAns(userAns)
        print("\nCongrats, it took you {} tries".format(str(self.tries)))


def main():
    game = Game()
    game.menu()


if __name__ == "__main__":
    main()
