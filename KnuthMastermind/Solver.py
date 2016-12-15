from Bot import Game
from random import randint
"""
Implementation of Knuth's algorithm for Mastermind
Expansion on the small game they made us do freshman year
Summer 2015
"""


class Solver:
    def __init__(self):
        self.solutions = self.genSolutions()
        self.solutionsSize = len(self.solutions)
        self.digitVal = 4
        self.maxVal = 9999

    def genSolutions(self):

        # why does class have noattribue maxVal?

        # generate all possible values
        returnAmount = ["%04d" % i for i in range(9999)]

        # convert them into list and each char into an int
        return [[int(number) for number in list(strings)] for strings in returnAmount]

    def updateSolutions(self):
        game = Game.Game()
        game.genAns()

        theTup = (0, 0)

        # This needs optimization
        while (len(self.solutions) > 1):

            attempt = []
            if len(self.solutions) == self.solutionsSize:
                # first try
                attempt = [1,2,3,4]

            elif theTup == (0,0):
                newPos = randint(0, len(self.solutions)-1)
                attempt = self.solutions[newPos]
            else:
                newPos = int(len(self.solutions)/2)
                attempt = self.solutions[newPos]


            theBool, theTup = game.checkAns(attempt)



            print(len(self.solutions))
            self.removeAns(attempt, theTup)




        game.checkAns(self.solutions[0], printStats=True)
    """
    def removeZZ(self, guess):
        currPos = 0
        for solution in self.solutions:
            if(self.findMatches(solution, guess, (0,0))):
                self.solutions.pop(currPos)
            currPos += 1
    """

    def findMatches(self, testAns, guess, guessTup):
        """
        Almost exactly the same to he check ans only here it returns the inSpot, inList
        this is used to find all other possibilities capable of matching

        Consider an initial value X
        we compare X to the answer and get a inSpot a, inList b
        After we eliminate from the list of all
        possiblities for any Xn that when compared to X doesnt create the same
        a, b par, after randomlly pick a different one and compare it again.

        What this is asking is "what if this was the answer then id have to get the same output
        """
        inSpot = 0
        inList = 0

        valMount = {value: testAns.count(value) for value in testAns}
        myMount = {value: 0 for value in guess}

        for i in range(len(guess)):
            if (guess[i] == testAns[i]):
                myMount[guess[i]] += 1
                inSpot += 1

        for i in range(len(guess)):
            if guess[i] != testAns[i] and guess[i] in testAns and myMount[guess[i]] < valMount[guess[i]]:
                myMount[guess[i]] += 1
                inList+=1

        if (inSpot,inList) == guessTup:
            return True

        return False

    def removeAns(self, guess, guessTup):
        pos = 0
        for solution in self.solutions:
            if(not self.findMatches(solution, guess, guessTup)):
                self.solutions.pop(pos)
            pos += 1

ai = Solver()
ai.updateSolutions()
