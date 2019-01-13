from populations.individual import Individual
from utilities.rnd import rndChance
from utilities.rnd import rndRange
from typing import List

def psm(individual, mutationChance):
    lengthOfNodes = len(individual.nodes)-1
    for index in range(lengthOfNodes):
        if (rndChance() < mutationChance):
            swapIndex = rndRange(0, lengthOfNodes)
            individual.nodes[index], individual.nodes[swapIndex] = individual.nodes[swapIndex], individual.nodes[index]
    return individual