from populations.population import Population
from populations.individual import Individual
from typing import List
from selections.tournament import tournament
from crossovers.ox import ox


def cycle(population: Population, nodes: List[List[int]], tournamentPlayersNumber:int = 3):
    newPop = []
    firstParent: Individual
    secondParent: Individual
    populationNumber = len(population.individuals)
    for _ in range(int(populationNumber/2)):
        firstParent = tournament(nodes, population, tournamentPlayersNumber)
        secondParent = tournament(nodes, population, tournamentPlayersNumber)
        child1: Individual = ox(firstParent, secondParent)
        child2: Individual = ox(secondParent, firstParent)
        newPop.extend([child1, child2])
        
    population.individuals = newPop