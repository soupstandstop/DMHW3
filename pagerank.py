import numpy as np

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

def PageRank(A, n, epsil, d):
    v = np.random.rand(n, 1)
    v = v / np.linalg.norm(v, 1)
    change_v = np.ones((n, 1), dtype=np.float32) * 100
    A_H = (d * A) + (((1-d)/n) * (np.ones((n,n), dtype=np.float32)))
    
    flag = False
    for i in range(max_iterations):
        change_v = v
        v = np.dot(A_H, v)
        if np.linalg.norm(v-change_v, 2) < epsil:
            flag = True
            cnt = i
            break
    if flag:
        print("finished in %s iterations!" % cnt)
    else:
        print("finished out of 100 iterations!")
    return v

PageRank(A, num_ver, min_epsilon, damping)