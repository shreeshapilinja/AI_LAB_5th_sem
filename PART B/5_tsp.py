from sys import maxsize
from itertools import permutations

def tsp(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    min_path = maxsize
    nextp = permutations(vertex)
    for i in nextp:
        cost = 0
        k = s
        for j in i:
            cost += graph[k][j]
            k=j
        cost += graph[k][s]
        min_path = min(min_path,cost)
    return min_path
v=4
graph = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
s=0
print(tsp(graph,s))
