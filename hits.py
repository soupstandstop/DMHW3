import math
import numpy as np

graph_1 = './data/graph_1.txt'
graph_2 = './data/graph_2.txt'
graph_3 = './data/graph_3.txt'
graph_4 = './data/graph_4.txt'
graph_5 = './data/graph_5.txt'
graph_6 = './data/graph_6.txt'
hw1 = './data/hw1.txt'

max_iterations = 100  
min_delta = 0.0001 
### 將點跟邊加入到ver & edge

num_lines = num_lines = sum(1 for line in open(graph_1))
ver = []
inedge = [[] for i in range(num_lines)]

graph = open(graph_1, 'r')
cnt = 0
for line in graph:
    tmp = line.split(',')
    ver0 = tmp[0].replace('\n', '')
    ver1 = tmp[1].replace('\n', '')
    ver.append(ver0)
    ver.append(ver1)
    inedge[cnt].append(ver0)
    inedge[cnt].append(ver1)
    cnt += 1
    
ver = list(set(ver))
num_ver = len(ver)

def E_matrix(num_ver, inedge):
    M = np.zeros(shape=(num_ver, num_ver))
    for i in inedge:
        M[int(i[0])-1][int(i[1])-1] = 1
    return M

A = E_matrix(num_ver, inedge)

auth = {}
hub = {}
for i in ver:
    auth[i] = 1
    hub[i] = 1

def hits(v, t, delta):
    flag = False
    for i in range(t):
        norm = 0
        change = 0.0
        tmp = {}
        tmp = auth.copy()
        for page in ver:
            auth[page] = 0
            for item in inedge:
                if item[1] == page:
                    auth[item[1]] += hub[item[0]]
                else:
                    pass
            norm += auth[page] ** 2
            
        norm = math.sqrt(norm)
        for page in ver:
            auth[page] = auth[page] / norm
            change += abs(tmp[page] - auth[page])
        
        norm = 0
        tmp = hub.copy()
        for page in ver:
            hub[page] = 0
            for item in inedge:
                if item[0] == page:
                    hub[item[0]] += auth[item[1]]
            norm += hub[page] ** 2
        
        norm = math.sqrt(norm)
        for page in ver:
            hub[page] = hub[page] / norm
            change += abs(tmp[page] - auth[page])
            
        print("This is NO.%s iteration" % (i + 1))
        print("authority", auth)
        print("hub", hub)
        if change < min_delta:
            flage = True
            break
    if flag:
        print("finished in %s iterations!" % (i + 1))
    else:
        print("finished out of 100 iterations!")

    print("The best authority page: ", max(auth.items(), key=lambda x: x[1]))
    print("The best hub page: ", max(hub.items(), key=lambda x: x[1]))
    return 0

hits(ver,max_iterations, min_delta)