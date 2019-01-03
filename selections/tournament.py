from utilities.rnd import rndChoices

from populations.individual import Individual
from populations.population import Population


def tournament(nodes, population, k = 3):
  indices = rndChoices(population.individuals, k)
  return min(indices, key=lambda x: x.calcFitness(nodes))