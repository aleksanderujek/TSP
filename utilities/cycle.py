from populations.population import Population
from populations.individual import Individual
from typing import List
from selections.tournament import tournament


def cycle(population: Population, nodes: List[List[int]], tournamentPlayersNumber:int = 3):
    newPop = []
    populationNumber = len(population.individuals)
    for _ in range(int(populationNumber/2)):
        parent1: Individual = tournament(nodes, population, tournamentPlayersNumber)
        parent2: Individual = tournament(nodes, population, tournamentPlayersNumber)
        newPop.append(parent1)
        newPop.append(parent2)
    population.individuals = newPop