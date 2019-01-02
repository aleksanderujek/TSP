from populations.individual import Individual
from populations.population import Population
from utilities.fetch import fetchFromFile
from utilities.fetch import fetchFromRemote
from utilities.factory import factory
from utilities.formatFile import formatString
from utilities.cycle import cycle
from timeit import default_timer as timer
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

response: str = fetchFromRemote(config['File']['Source']) if config['File']['Type'] == 'url' else fetchFromFile(config['File']['Source'])

nodes, numberOfNodes = formatString(response)

individualFactory = factory(Individual)(numberOfNodes)

start = timer()
Pop = Population(int(config['Algorithm']['PopulationNumber']), individualFactory)
tournamentPlayersNumber = int(config['Algorithm']['NumberOfPlayersInTournament'])
generationNumber = int(config['Algorithm']['Generations'])
time = int(config['Algorithm']['Time'])
crossoverRatio = float(config['Algorithm']['CrossOverRatio'])
mutationRatio = float(config['Algorithm']['MutationRatio'])
i: int = 0
best = 10000000
while i < generationNumber and timer()-start < time:
    # print('GENERACJA : ', i)
    Pop = cycle(Pop, nodes, tournamentPlayersNumber, crossoverRatio, mutationRatio)
    currentBest = Pop.getBest(nodes).calcFitness(nodes)
    if currentBest<best:
        best = currentBest
        print(best)
    i+= 1
End = timer()
print(End - start)
print('Ostateczna liczba generacji: ', i)