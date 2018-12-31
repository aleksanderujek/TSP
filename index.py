from populations.individual import Individual
from populations.population import Population
from utilities.fetch import fetchFromFile
from utilities.factory import factory
from utilities.formatFile import formatString
from utilities.cycle import cycle
from timeit import default_timer as timer

response: str = fetchFromFile('src/berlin52.txt')

nodes, numberOfNodes = formatString(response)

individualFactory = factory(Individual)(numberOfNodes)

start = timer()
Pop = Population(40, individualFactory)
tournamentPlayersNumber = 3
for i in range(10000):
    cycle(Pop, nodes, tournamentPlayersNumber)
End = timer()
print(End - start)