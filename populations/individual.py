from typing import List
from random import shuffle

class Individual:
  nodes: List[int] = []
  fitness = -1
  
  def __init__(self, numberOfNodes = None):
    if numberOfNodes is not None:
      self.nodes: List[int] = list(range(numberOfNodes))
      shuffle(self.nodes)

  def calcFitness(self, distanceArray):
    if self.fitness == -1:
        prevNode = None
        self.fitness = 0
        for node in self.nodes:
            if prevNode is not None:
                self.fitness += distanceArray[prevNode][node]
            prevNode = node
        self.fitness += distanceArray[prevNode][self.nodes[0]]
    return self.fitness