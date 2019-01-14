#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import string
from math import sqrt

def createMatrix(rows):
    matrix = [[0 for col in range(int(rows[0]))] for row in range(int(rows[0]))]
    i = 0
    for w in rows[1:]:
        w = string.strip(w).split(' ')
        j = 0
        for odl in w:
            matrix[i][j] = int(odl)
            matrix[j][i] = int(odl)
            j+=1
        i+=1

    return matrix

def calculateDistance(route, matrix):
    distance = 0
    route = string.strip(route).split('-')
    try:
        route = list(map(int, route))
    except ValueError:
        pass
    for i in range(len(route)-1):
        distance+=matrix[route[i]][route[i+1]]
    distance+=matrix[route[len(route)-1]][route[0]]
    return distance

fileName = sys.argv[1]
resultsFileName = sys.argv[2]

inputFile = open(fileName, 'r') 
inputFile2 = open(resultsFileName, 'r') 

plikWy = open('spr_'+fileName.split('.')[0]+'.txt', 'w') 

rows = inputFile.readlines() 
inputFile.close()

matrix = createMatrix(rows)

output = inputFile2.readlines() 
inputFile2.close()

for w in output:
    distance = 0
    w = string.strip(w).split(' ') 
    if len(w)==2:
        distance = calculateDistance(w[0], matrix)
        result = "%i %i %s" % (distance, int(w[1]), distance==int(w[1]))
    else:
        result = "Pominięto: %s" % w
    print result
    plikWy.write(result+'\n')
plikWy.close()