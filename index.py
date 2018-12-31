from populations.individual import Individual
from populations.population import Population
from utilities.fetch import fetchFromFile
from utilities.factory import factory
from utilities.formatFile import formatString
from timeit import default_timer as timer
from selections.tournament import tournament

response: str = fetchFromFile('src/berlin52.txt')

nodes, numberOfNodes = formatString(response)

individualFactory = factory(Individual)(numberOfNodes)


start = timer()
Pop = Population(40, individualFactory)
tournamentPlayersNumber = 3
for i in range(10):
    Pop.individuals = [tournament(nodes, Pop, tournamentPlayersNumber) for _ in Pop.individuals]
End = timer()
print(End - start)