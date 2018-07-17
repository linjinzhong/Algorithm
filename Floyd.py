#=========================最短路径(Floyd)===========================
#  解决全源最短路径问题：
# for k in [1,N]:
#   以k为中介点，枚举所有顶点对(i,j) 
#   for i in [1,N]:
#       for j in [1,N]:
#           if d[i][k]+d[k][j] < d[i][j]:
#               d[i][j] = d[i][k] + d[k][j]

def Floyd(G, N):
    dis = [[float('inf')]*N for _ in range(N)]
    for k in range(N):
        dis[k][k] = 0
    #  输入顶点间的距离
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]