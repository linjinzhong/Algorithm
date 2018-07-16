#=========================并查集===========================


# 寻找x的根节点，寻找完毕后将子节点都指向根节点
def findFather(x):
    a = x
    while x != father[x]:
        x = father[x]
    # 路径压缩,可不写，把查找根节点过程中的所有子节点指向根节点，即找到的x
    while a != father[x]:
        t = a
        a = father[a]
        father[t] = x

    return x

# 合并过程将较小节点设为根节点
def union(x,y):
    faA = findFather(x)
    faB = findFather(y)
    if faA < faB:
        father[faB] = faA
    elif faA > faB:
        father[faA] = faB


if __name__ == '__main__':
    N = 10
    father = list(range(N+1))
    isRoot = [False]*(N+1)

    R = ((4,3),(5,6),(6,7))
    for x,y in R:
        # print(x,y)
        union(x,y)
    print(father)
    for i in range(1,N+1):
        isRoot[findFather(i)] = True

    print(sum(isRoot[1:]))
    print(father)



