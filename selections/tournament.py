import random

from populations.individual import Individual
from populations.population import Population


def tournament(nodes, population, k = 3):
  indices = random.choices(population=population.individuals, k=k)
  return min(indices, key=lambda x: x.calcFitness(nodes))