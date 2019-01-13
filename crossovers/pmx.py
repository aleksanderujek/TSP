import random as rnd
from populations.individual import Individual
from typing import List

def pmx(firstParent, secondParent):
    child: Individual = firstParent
    tempChild: List[int] = []
    firstIndex = rnd.randint(0,len(child.nodes)-1)
    secondIndex = rnd.randint(firstIndex, len(child.nodes)-1)
    for i in range(firstIndex, secondIndex):
        child.nodes[i] = firstParent.nodes[i]
        tempChild.append(firstParent.nodes[i])
        
    
    return child
    

