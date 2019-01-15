from populations.individual import Individual
from populations.population import Population
from utilities.fetch import fetchFromFile
from utilities.factory import factory
from utilities.formatFile import formatString
from utilities.cycle import cycle
from timeit import default_timer as timer
import configparser
import os
import datetime


config = configparser.ConfigParser()
config.read('config.ini')

response = fetchFromFile(config['File']['Source'])

nodes, numberOfNodes = formatString(response)

individualFactory = factory(Individual)(numberOfNodes)
os.system('clear')
start = timer()
Pop = Population(int(config['Algorithm']['PopulationNumber']), individualFactory)
tournamentPlayersNumber = int(config['Algorithm']['NumberOfPlayersInTournament'])
generationNumber = int(config['Algorithm']['Generations'])
time = float(config['Algorithm']['Time'])
crossoverRatio = float(config['Algorithm']['CrossOverRatio'])
mutationRatio = float(config['Algorithm']['MutationRatio'])
displayTime = float(config['Algorithm']['DisplayTime'])
currentTime = 0
i = 0
best = Individual(None)
bestFitness = 10000000
while i < generationNumber or timer()-start < time:
    Pop = cycle(Pop, nodes, tournamentPlayersNumber, crossoverRatio, mutationRatio, i)
    currentBest = Pop.getBest(nodes)
    currentBestFitness = currentBest.calcFitness(nodes)
    if currentBestFitness<bestFitness:
        best = currentBest
        bestFitness = currentBestFitness
    if timer()-start > currentTime:
        print(bestFitness)
        currentTime += displayTime
    i+= 1
End = timer()
print('Najlepszy: ', bestFitness)
myList = '-'.join(map(str, best.nodes))
now = datetime.datetime.now()
fileName = 'src/' + config['File']['ResultFileName'] + '-' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ':' + str(now.microsecond) + '.txt'
f= open(fileName,"w+")
f.write(myList + ' ' + str(bestFitness))
f.close()
print(End - start)
print('Ostateczna liczba generacji: ', i)