#=========================图的遍历===========================
from collections import deque
# ===============深度遍历=========================
def DFS(u, depth):
    vis[u] = True   #设置u已被访问
    #这里可以对u进行一些操作
    #下面对u出发所能到达的顶点进行枚举
    for v in range(N):
        if vis[v] == False and G[u][v] != float('inf'):
            DFS(v, depth + 1)

def DFSTraverse():
    for u in range(N):
        if vis[u] == False:
            DFS(u,1)


# ===============广度遍历=========================
def BFS(deq):
    while deq:
        u = deq.popleft()
        for v in range(N):
            if inQ[v] == False and G[u][v] != float('inf'):
                deq.append(v)
                inQ[v] = True

def BFSTraverse():
    for u in range(N):
        if inQ[u] == False: #如果u未曾入队
            deq = deque([u])
            inQ[u] = True
            BFS(deq) #遍历u所在的联通块


if __name__ == '__main__':
    N = 10
    vis = [False]*N  #顶点是否已被访问标记
    G = [[float('inf')]*N for _ in range(N)]
    print(G)



