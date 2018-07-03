#=======================分治算法========================
'''
分治算法分为两步，一步是divide，一步是conquerd。
分治法没有重叠子问题，解决的问题不一定是最优化问题。比如归并排序和快速排序都是分别处理左右序列。
'''

#=======================最近点对问题====================
'''
假设在坐标平面上分布了一系列的点，那么问题是求取这些点两两之间的最短距离。
首先对于所有的点，按照x坐标将其分为两部分，这就是divide。
那么最短距离就是左边部分中的最短距离Dl，右边部分的最短距离Dr，以及左右部分之间的距离Dc。
对于Dl以及Dr，可以递归的计算得到，这就是conquer。那么唯一的问题就是Dc。
我们知道如果最短距离是Dc的话，那么Dc<=min（Dl，Dr）。
因此我们只需要计算距离divide分割线S = min（Dl，Dr）的点就可以了。
进一步我们可以看到对于每个在2S区域内的点，只需要计算y坐标距离这一点不大于S的点就可以。
'''
from math import sqrt

#求点对举距离
def get_distance(dots):
    return sqrt((dots[0][0]-dots[1][0])**2 + (dots[0][1]-dots[1][1])**2)

def nearest_dot(s):
    len = s.__len__()
    left = s[0:len//2]
    right = s[len//2:]
    mid_x = (left[-1][0] + right[0][0]) // 2.0
    if left.__len__() > 2:
        lmin = nearest_dot(left)    #左侧最近点对
    else:
        lmin = left
    if right.__len__() > 2:
        rmin = nearest_dot(right)   #右侧最近点对
    else:
        rmin = right

    if lmin.__len__() > 1:
        dis_1 = get_distance(lmin)
    else:
        dis_1 = float("inf")
    if rmin.__len__() > 1:
        dis_2 = get_distance(rmin)
    else:
        dis_2 = float('inf')

    d = min(dis_1, dis_2)   #最近点对距离

    mid_min = []
    for i in left:
        if mid_x - i[0] <= d:
            for j in right:
                if abs(i[0]-j[0]) <= d and abs(i[1]-j[1]) <= d:
                    if get_distance((i,j)) <= d:
                        mid_min.append([i,j])
    if mid_min:
        dic = []
        for i in mid_min:
            dic.append({get_distance(i):i})
        dic.sort(key=lambda x: x.keys())
        return list(dic[0].values())[0]
    elif dis_1 > dis_2:
        return rmin
    else:
        return lmin

def divide_conquer(s):
    s.sort(key = lambda x: x[0])
    nearest_dots = nearest_dot(s)
    print(nearest_dots)  

if __name__ == '__main__':
    s=[(0,1),(3,2),(4,3),(5,1),(1,2),(2,1),(6,2),(7,2),(8,3),(4,5),(9,0),(6,4)]
    divide_conquer(s)