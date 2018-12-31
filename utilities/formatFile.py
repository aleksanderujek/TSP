from typing import List

def formatString(string: str) -> (List[List[int]], int):
  lines = string.split('\n')
  numberOfNodes = int(lines.pop(0))
  nodes = []
  for i, line in enumerate(lines):
    elements = line.split(' ')
    elements.pop()
    nodes.append(elements)
    for j, element in enumerate(elements):
      if i != j:
        nodes[j].append(element)
  nodes = [list(map(int, x)) for x in nodes]
  return nodes, numberOfNodes