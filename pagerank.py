from pygraph.classes.digraph import digraph
from tqdm import tqdm
graph_1 = './data/graph_1.txt'
graph_2 = './data/graph_2.txt'
graph_3 = './data/graph_3.txt'
graph_4 = './data/graph_4.txt'
graph_5 = './data/graph_5.txt'
graph_6 = './data/graph_6.txt'
hw1 = './data/hw1.txt'

damping = 0.85
max_iterations = 100
min_epsilon = 0.00001
graph = digraph()

def PageRank():
    for node in graph.nodes(): # graph.nodes are all nodes in this graph
        #print(node)
        if len(graph.neighbors(node)) == 0:
            for node2 in graph.nodes(): # modify one node which do not have edge to have edges to all nodes
                digraph.add_edge(graph, (node, node2)) # add edges
    nodes = graph.nodes()
    graph_size = len(nodes)
    
    if graph_size == 0:
        return {}
    page_rank = dict.fromkeys(nodes, 1.0 / graph_size)
    damping_value = (1.0 - damping) / (graph_size)
    
    flag = False
    for i in range(max_iterations):
        change = 0
        for node in nodes:
            rank = 0
            for incident_page in graph.incidents(node):  
                rank += damping * (page_rank[incident_page] / len(graph.neighbors(incident_page)))
            rank += damping_value
            change += abs(page_rank[node] - rank)
            page_rank[node] = rank

        print("This is NO.%s iteration" % (i + 1))
        print(page_rank)

        if change < min_epsilon:
            flag = True
            break
    if flag:
        print("finished in %s iterations!" % node)
    else:
        print("finished out of 100 iterations!")
    return page_rank

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
            dg.add_edge((i, j))
            
            
page_ranks = PageRank()
print("The final page rank is\n", page_ranks)