from populations.individual import Individual
from utilities.rnd import rndChance
from utilities.rnd import rndRange
from typing import List

def rsm(individual, mutationChance):
    if (rndChance() < mutationChance):
        lengthOfNodes = len(individual.nodes)-1
        startIndex = rndRange(0, lengthOfNodes)
        endIndex = rndRange(startIndex, lengthOfNodes)
        individual.nodes[startIndex:endIndex] = reversed(individual.nodes[startIndex:endIndex])
    return individual