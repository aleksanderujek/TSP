import random
from populations.individual import Individual
from populations.population import Population

def getInterval(max, value):
  return max + 1 - value

def getHighestFitness(nodes, population):
  return max(population.individuals, key=lambda x: x.calcFitness(nodes)).calcFitness(nodes)

def getWinnerInterval(pool):
  rnd = random.randint(0, pool[-1])
  winner = 0
  for i in range(0, len(pool)-1):
    if rnd < pool[i+1]:
      winner = i
      break
  return winner

def roulettePool(nodes, population, highestFitness):
  prev = 0
  pool = [0]
  for individual in population.individuals:
    pool.append(prev + getInterval(highestFitness, individual.calcFitness(nodes)))
    prev += getInterval(highestFitness, individual.calcFitness(nodes))
  return pool

def roulette(nodes, population):
  return population.individuals[getWinnerInterval(roulettePool(nodes, population, getHighestFitness(nodes, population)))]