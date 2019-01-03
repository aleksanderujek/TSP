from populations.population import Population
from populations.individual import Individual
from typing import List
from selections.tournament import tournament
from crossovers.ox import ox
from mutations.psm import psm
from utilities.rnd import rndChance

def percentageChance(ratio):
    return True if ratio>rndChance() else False

def cycle(population: Population, nodes: List[List[int]], tournamentPlayersNumber:int = 3, crossoverRatio = 0.95, mutationRatio = 0.05):
    newPop = []
    firstParent: Individual
    secondParent: Individual
    populationNumber = len(population.individuals)
    for _ in range(int(populationNumber/2)):
        firstParent = tournament(nodes, population, tournamentPlayersNumber)
        secondParent = tournament(nodes, population, tournamentPlayersNumber)
        child1: Individual = ox(firstParent, secondParent) if percentageChance(crossoverRatio) else firstParent
        child2: Individual = ox(secondParent, firstParent) if percentageChance(crossoverRatio) else secondParent
        # print(child1.calcFitness(nodes))
        # print(child2.calcFitness(nodes))
        child1 = psm(child1, mutationRatio)
        child2 = psm(child2, mutationRatio)
        newPop.extend([child1, child2])
    population.individuals = newPop
    return population