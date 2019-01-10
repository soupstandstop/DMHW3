import numpy as np

graph_1 = './data/graph_1.txt'
graph_2 = './data/graph_2.txt'
graph_3 = './data/graph_3.txt'
graph_4 = './data/graph_4.txt'
graph_5 = './data/graph_5.txt'
graph_6 = './data/graph_6.txt'
hw1 = './data/hw1.txt'

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

def simrank(M, num, c=.1, t=100):
    S = np.identity(num_ver) # similarity matrix
    I = np.identity(num_ver) # identity matrix
    #W = M/M.sum(0) # 除以總入邊點數
    W = np.zeros(shape=(num,num))
    b = M.sum(0)
    for j in range(num):
        for i in range(num):
            if b[j]==0:
                pass
            else:
                W[i][j] = M[i][j]/b[j]
    
    for i in range(t):
        S = c*np.dot(np.dot(W.T, S), W) + (1-c)*I
    for i in range(num_ver):
        S[i][i] = 1
    return S

n = num_ver
a = E_matrix(n, inedge)

simrank(a, n)