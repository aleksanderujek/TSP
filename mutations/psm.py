from populations.individual import Individual
import random as rnd
from typing import List

def psm(individual: Individual):
    mutatedIndividual: Individual = Individual(None)
    lastIndex = len(individual.nodes)
    firstIndex = rnd.randint(0,lastIndex)
    secondIndex = rnd.randint(firstIndex, lastIndex)
    startSet: List[int] = []
    innerSet: List[int] = []
    endSet: List[int] = []
    # First part
    startSet = individual.nodes[0:firstIndex]
    # Shuffled part
    innerSet = individual.nodes[firstIndex:secondIndex]
    rnd.shuffle(innerSet)
    # Last part
    endSet = individual.nodes[secondIndex:lastIndex]
    mutatedIndividual.nodes = startSet + innerSet + endSet
    return mutatedIndividual