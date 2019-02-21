# Python genetic algorithm implementation for TSP
Project was made to pass University class. I've chosen Python due to his performance.

## Implemented and used operators ⚙️
For better performance and due to limited time I used this operators:
- `Selection`: Tournament
- `Crossovers`: OX algorithm
- `Mutations`: RSM algorithm

To pass the class I had to implement two selection methods. Beside tournament selection, I've implemented roulette selection. Roulette selection was very slow at the begining of the GA, so in `config` file is `tournament` as default selection.

## Config file 🛠
I've prepared `config.ini` file to quickly change things like:
- Source file (`town problem`)
- Name of the results file
- Population number
- Number of players in tournament
- Generations
- Time
- Crossover ratio
- Mutation ratio
- Display time between current best individual

## How to use? 
You have two possibilities to use this.
1. Use default python3 compiler, by simply typing:
```python
python3 index.py
```
2. Use pypy as compiler:
```
pypy3 index.py
```

## Results ⏳


## Output format
After executing the program with proper config file, program will save the best route (based on fitness) to file, named with format from config file. To make the files completely unique program add `timestamp` to the name of the file. 
Content of the file:  
* Route seperated with `-` char
* Fitness of the route

Example:  
```
4-8-11-5-27-0-20-12-15-23-7-26-22-6-24-18-10-21-13-16-17-14-3-9-19-1-2-28-25 2020
```
## Licence 🗄
Project is under MIT Licence 
