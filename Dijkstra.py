#=========================最短路径(Dijkstra)===========================
# 对于任意给出的图G(V,E)和起点S，终点T,如何求从S到T的最短路径。
# Dijkstra用来解决单源最短路劲问题，基本思想：对图G(V,E)设置集合S,
# 存放已被访问过的顶点，然后每次从集合V-S中选择与起点s的最短距离最小的一个顶点
# (记为u)，访问并加入集合。之后令顶点u为中介点，优化起点s与所有能通过u到达
# 顶点v之间的最短距离。这样操作执行n次(顶点个数)，直到集合S包含所有顶点。
# 伪代码：
# def Dijkstra(s):
#     # 初始化
#     for i in range(N):
#         u = 使d[u]最小且未被访问过的顶点标号
#         记u为已被访问
#         for 从u出发所能到达的所有顶点v:
#             if v未被访问 and 以u为中介点是s到达顶点v的最短距离d[v]更优:
#                 优化d[v]

# 邻接矩阵版本
def Dijkstra(G, s, N):
    d = [float('inf')]*N    #起点到各顶点的距离
    vis = [False]*N         #顶点是否被访问过
    d[s] = 0                #起点到自身的距离为0
    #从起点到顶点v的最短路径上v的前一个顶点,初始化为自身
    preVertex = [[i] for i in range(N)]
    for i in range(N):      #循环N次
        u, MIN = None, float('inf') #u使得d[u]最小，MIN存放最小的d[u]
        for j in range(N):  #找到未访问顶点中d[]最小的
            if vis[j] == False and d[j] < MIN:
            u, MIN = j, d[j]

        #找不到小于INF的d[u],说明剩下的顶点与起点s不连通
        if u is None:
            return
        vis[u] = True       #标记u已被访问
        # 优化d
        for v in range(N):
            # 如果v未被访问并且uv联通且以u为中介点到达v可以使原d[v]更优
            if vis[v] == False and G[u][v] != float('inf'):
                newD = d[u] + G[u][v]
                if newD < d[v]:
                    d[v] = newD
                    pre[v].clear()      #有更优前驱，清空之前前驱
                    pre[v].append(u)    #u为v的前驱
                elif newD == d[v]:
                    pre[v].append(u)    #如果u作为前驱效果和原来一样，则也添加



# 在第一标尺相同情况下第二标尺选择路径：第一标尺为距离，第二标尺有以下三种：

# 每条边增加一个边权(花费等)，要求在最短路径下花费最少，cost[N][N]。
# 修改优化部分代码,初始化c[N]为inf，只有c[s]为0.
        # # 优化d
        # for v in range(N):
        #     # 如果v未被访问并且uv联通且以u为中介点到达v可以使原d[v]更优
        #     if vis[v] == False and G[u][v] != float('inf'):
        #         newD = d[u] + G[u][v]
        #         if newD < d[v]:
        #             d[v] = newD
        #             c[v] = c[u] + cost[u][v]
        #         elif newD == d[v] and c[u] + cost[u][v] < c[v]:
        #             c[v] = c[u] + cost[u][v]
# 给每个点增加一个点权(每个城市的物资)，点权之和最大
# 新增点权：weight表示城市u中的物资数目
# 增加数组w表示起点s到顶点u可以收到的最大物资数。
# 初始化只有w[s]为weight[s],其他为0。
        # # 优化d
        # for v in range(N):
        #     # 如果v未被访问并且uv联通且以u为中介点到达v可以使原d[v]更优
        #     if vis[v] == False and G[u][v] != float('inf'):
        #         newD = d[u] + G[u][v]
        #         if newD < d[v]:
        #             d[v] = newD
        #             w[v] = w[u] + weight[v]
        #         elif newD == d[v] and w[u] + weight[v] < w[v]:
        #             w[v] = w[u] + weight[v]
# 最短路径条数
# 只需增加一个num数组
# 初始化只有num[s] = 1,其余num[u]均为0
        # 优化d
        for v in range(N):
            # 如果v未被访问并且uv联通且以u为中介点到达v可以使原d[v]更优
            if vis[v] == False and G[u][v] != float('inf'):
                newD = d[u] + G[u][v]
                if newD < d[v]:
                    d[v] = newD
                    num[v] = num[u]
                elif newD == d[v]:
                    num[v] += num[u]