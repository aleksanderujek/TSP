from populations.population import Population
from populations.individual import Individual
from typing import List
from selections.tournament import tournament
from selections.roulette import roulette
from crossovers.ox import ox
from mutations.rsm import rsm
from utilities.rnd import rndChance

def percentageChance(ratio):
    return True if ratio>rndChance() else False

def cycle(population: Population, nodes: List[List[int]], tournamentPlayersNumber:int = 3, crossoverRatio = 0.95, mutationRatio = 0.05, generationIndex = 0):
    newPop = []
    populationNumber = len(population.individuals)
    for _ in range(int(populationNumber/2)):
        firstParent = tournament(nodes, population, tournamentPlayersNumber)
        secondParent = tournament(nodes, population, tournamentPlayersNumber)
        child1 = ox(firstParent, secondParent) if percentageChance(crossoverRatio) else firstParent
        child2 = ox(secondParent, firstParent) if percentageChance(crossoverRatio) else secondParent
        child1 = rsm(child1, mutationRatio)
        child2 = rsm(child2, mutationRatio)
        newPop.extend([child1, child2])
    population.individuals = newPop
    return population