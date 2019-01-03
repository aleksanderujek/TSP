from utilities.rnd import rndRange
from typing import List
from populations.individual import Individual
def ox(parent1, parent2):
    child: Individual = Individual(None)
    child.nodes = []
    firstIndex = rndRange(0,len(parent1.nodes)-1)
    secondIndex = rndRange(firstIndex, len(parent1.nodes)-1)
    innerSet: List[int] = parent1.nodes[firstIndex:secondIndex]
    startSet: List[int] = []
    endSet: List[int] = []
    for _, value in enumerate([item for item in parent2.nodes if item not in innerSet]):
        if len(startSet)<firstIndex:
            startSet.append(value)
        else:
            endSet.append(value)
    child.nodes = startSet + innerSet + endSet
    return child