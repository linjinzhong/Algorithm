#=========================拓扑排序===========================
# 有向无环图：有向图的任意顶点都无法通过一些有向边回到自身
# 拓扑排序: 将有向无环图G的所有顶点排成一个线性序列，使得对图G中任意两个顶点u,v，
# 如果存在有向边u->v，那么在序列中u一定在v的前面。这个序列叫做拓扑排序。
# 使用邻接表实现:
# 记录结点的入度,建立数组inDegr[N]
# 定义一个队列， 将所有入度为0的顶点加入队列
# 取队首结点输出，删除它的有向边，并令这些边到达的顶点的入度减1,如果某个顶点减到0则加入队列。
# 反复上述操作直到队列为空，如果此时入队结点恰好为N，那么说明拓扑排序成功，图G是有向无环图。
# 如果要求多个入度为0的顶点时， 选择编号最小的顶点，可以使用优先队列或者有序集合。

from collections import deque
def  topologicalSort(inDegree, G, N):
    n = 0
    deq = deque()
    # 将所有入度为0的顶点加入队列
    for i in range(N):
        if inDegree[i] == 0:
            deq.append(i)
    while deq:
        u = deq.popleft()
        for i in range(len(G[u])):
            v = G[u][i]     #u的后继结点v
            inDegree[v] -= 1
            if inDegree[v] == 0:
                deq.append(v)
        G[u].clear()    #清空u的出边，可不写
        n += 1
    if n == N:
        return True
    return False