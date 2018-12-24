from pygraph.classes.digraph import digraph
import math
import pandas as pd
import numpy as np
from tqdm import tqdm

graph_1 = './data/graph_1.txt'
graph_2 = './data/graph_2.txt'
graph_3 = './data/graph_3.txt'
graph_4 = './data/graph_4.txt'
graph_5 = './data/graph_5.txt'
graph_6 = './data/graph_6.txt'
hw1 = './data/hw1.txt'

max_iterations = 100  
min_delta = 0.0001  
graph = digraph()

def hits():
    hub = {}
    authority = {}
    for node in graph.nodes():
        hub[node] = 1
        authority[node] = 1
    if not graph:
        return

    flag = False
    for i in range(max_iterations):
        change = 0.0 
        norm = 0 
        tmp = {}
        tmp = authority.copy()
        for node in graph.nodes():
            authority[node] = 0
            for incident_page in graph.incidents(node):  
                authority[node] += hub[incident_page]
            norm += pow(authority[node], 2)

        norm = math.sqrt(norm)
        for node in graph.nodes():
            authority[node] /= norm
            change += abs(tmp[node] - authority[node])

        norm = 0
        tmp = hub.copy()
        for node in graph.nodes():
            hub[node] = 0
            for neighbor_page in graph.neighbors(node):  
                hub[node] += authority[neighbor_page]
            norm += pow(hub[node], 2)

        norm = math.sqrt(norm)
        for node in graph.nodes():
            hub[node] /= norm
            change += abs(tmp[node] - hub[node])

        print("This is NO.%s iteration" % (i + 1))
        print("authority", authority)
        print("hub", hub)

        if change < min_delta:
            flag = True
            break
    if flag:
        print("finished in %s iterations!" % (i + 1))
    else:
        print("finished out of 100 iterations!")

    print("The best authority page: ", max(authority.items(), key=lambda x: x[1]))
    print("The best hub page: ", max(hub.items(), key=lambda x: x[1]))

data = []
edge = {}

file = open(graph_1, 'r')   # Modify this line from graph_1 to graph_6 
for line in file:
    if ',' in line:
        line = line.split(',')
        line[1] = line[1].replace('\n', '')
        data.append(line[0])
        data.append(line[1])
        #print(line[0])
        edge[line[0]] = []
        edge[line[0]].append(line[1])
    else:
        line = line.split()
        data.append(line[0])
        data.append(line[1])
    #print(line[1])
data = list(set(data))
data = sorted(data)
file.close()

graph = digraph()
dg = graph
dg.add_nodes(data)
with tqdm(total = len(edge)) as pbar:
    for i in edge:
        pbar.update(1)
        for j in edge[i]:
            #print(i, j)
            dg.add_edge((i, j))
            
hits = hits()
print(hits)