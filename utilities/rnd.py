import random as rnd

def rndRange(first,last):
    return rnd.randint(first,last)

def rndChance():
    return rnd.random()

def rndShuffle(listToShuffle):
    return rnd.shuffle(listToShuffle)

def rndChoices(listOfChoices, numberOfElements):
    return [rnd.choice(listOfChoices) for _ in range(numberOfElements)]