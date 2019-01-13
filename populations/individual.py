from typing import List
from utilities.rnd import rndShuffle

class Individual:
  nodes = []
  fitness = -1
  
  def __init__(self, numberOfNodes = None):
    if numberOfNodes is not None:
      self.nodes = list(range(numberOfNodes))
      rndShuffle(self.nodes)

  def calcFitness(self, distanceArray):
    if self.fitness == -1:
        prevNode = None
        self.fitness = 0
        for node in self.nodes:
            if prevNode is not None:
                self.fitness += distanceArray[prevNode][node]
            prevNode = node
        self.fitness += distanceArray[self.nodes[-1]][self.nodes[0]]
    return self.fitness