########################Sort Algorithm######################

# ######################插入排序#############################
# 直接插入排序
'''
将一个记录插入到之前已排好序的有序表中，默认将第一个元素看作有序表，依次插入后边的所有元素。
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定，适合小数组
'''
def strInsertSort(L):
    for i in range(1,len(L)):
        tmp, j = L[i], i-1
        while j >= 0 and tmp < L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = tmp
    # return L

# 折半插入排序
'''
基于直接插入改写，减少“移动”和“比较”次数。
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定
'''
def bInsertSort(L):
    for i in range(1,len(L)):
        tmp, j = L[i], i-1
        l, r = 0, i-1
        while (l <= r):
            m = (l + r) // 2
            if tmp < L[m]:
                r = m - 1
            else:
                l = m + 1
        while j > r:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = tmp

# 希尔排序
'''
直接对插入排序进行改进，又称“缩小增量排序”
时间复杂度：O(n^2)
空间复杂度：O(1)
不稳定
'''
def shellInsertSort(L):
    step = len(L) // 2
    while step >= 1:
        for i in range(step,len(L)):
            tmp, j = L[i], i-step
            while j >= 0 and tmp < L[j]:
                L[j+step] = L[j]
                j -= step
            L[j+step] = tmp
        step //= 2


# ######################交换排序#############################
# 冒泡排序
'''
两两比较相邻元素，第一次冒上来的是最小的元素，第二次是次小。
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定
'''
def bubbleSort(L):
    for i in range(0, len(L)):
        for j in range(len(L)-1,i,-1):
            if L[j] < L[j-1]:
                L[j-1], L[j] = L[j], L[j-1]

# 快速排序
'''
通过一趟排序将元素分割成两个部分，左半部分比关键元素小，右半部分比关键元素大。即能确定关键元素最终所在位置。
时间复杂度：O(nlogn),最坏情况O(n^2)
空间复杂度：O(1)
不稳定
'''
def quickSort(L, l, r):
    if (l < r):
        i, j, x = l, r, L[l]
        while i < j and L[j] >= x:
            j -= 1
        if i < j:
            L[i] = L[j]
            i += 1
        while i < j and L[i] <= x:
            i += 1
        if i < j:
            L[j] = L[i]
            j -= 1
        L[i] = x
        quickSort(L, l, i-1)
        quickSort(L, i+1, r)


# ######################选择排序#############################
# 简单选择排序
'''
每一趟排序都会选出最小的(或最大的)值。
时间复杂度：O(n^2)
空间复杂度：O(1)
不稳定
'''
def simSelectSort(L):
    for i in range(0,len(L)):
        m = i
        for j in range(i+1,len(L)):
            if L[j] < L[m]:
                m = j
        L[i], L[m] = L[m], L[i]

# 堆排序
'''
利用堆这种数据结构的性质所设计的。
时间复杂度：O(nlogn)
空间复杂度：O(1)
'''
def heapAdjust(L, k, n):
    tmp, i = L[k], 2*k+1
    # 从k结点的左子结点i开始
    while i < n :
        if i + 1 < n and L[i] < L[i+1]:
            # i为左右子结点中最大一个的索引
            i = i + 1
        if L[i] > tmp:
            #如果子结点大于父结点，将子结点值赋值给父结点，不用交换
            L[k] = L[i]
            k = i
        else:
            break
        i = i * 2 + 1
    #将tmp放到最终位置
    L[k] = tmp

def heapSort(L):
    # 构造大顶堆，从0到n/2-1都有孩子结点
    for i in range(len(L)//2-1,-1,-1):
        heapAdjust(L,i,len(L))

    # 调整堆结构+交换堆顶元素与末尾元素
    for j in range(len(L)-1,0,-1):
        L[0], L[j] = L[j], L[0]
        heapAdjust(L,0,j)   #重新对堆进行调整


# ######################归并排序#############################
'''
将两个或两个以上的有序表组合成一个有序表，采用分治法实现
时间复杂度:O(nlogn)
空间复杂度：O(n)
稳定
'''
def merge(L, l, m, r):
    i, j, t = l, m+1, 0
    tmp = [0]*(r-l+1)
    while i <= m and j <= r:
        if L[i] <= L[j]:
            tmp[t] = L[i]
            i += 1
        else:
            tmp[t] = L[j]
            j += 1
        t += 1
    while i <= m:
        tmp[t] = L[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = L[j]
        t += 1
        j += 1
    t = 0
    while l <= r:
        L[l] = tmp[t]
        l += 1
        t += 1

def mergeSort(L, l, r):
    if l < r:
        m = (l+r) // 2
        mergeSort(L, l, m)
        mergeSort(L, m+1, r)
        merge(L, l, m, r)

# ######################基数排序#############################
# 基数排序
'''
依次按每个基数位上的数字排序，数字基数为10,字母基数为26。
每个基数位上数字排序分为：分配，收集两个过程
时间复杂度：O(d(n+r))
空间复杂度：O(n+r)
稳定
'''
#取数据i,d位上的数字
def getDigit(i, d):
    for _ in range(1,d):
        i //= 10
    return i % 10
'''
n:数据个数
radix:基数个数，数字为1-9总共10个基数，字母为a-z总共26个基数
dis:数据中最多基数个数，即最多位数。
'''
def radixSort(L, n, radix, dis):
    count = [0]*radix #每个基数存放数据个数
    bucket = [0]*n    #暂存数据
    for d in range(1,dis+1):
        #置空每个桶(基数)
        count = [0]*radix
        #统计每个桶所存放数据个数
        for j in range(n):
            count[getDigit(L[j], d)] += 1
        #计算每个桶的右边界索引
        for j in range(1,radix):
            count[j] += count[j-1]#count[i]表示第i个桶的右边界索引
        #分配数据
        for j in range(n):
            v = getDigit(L[j], d)
            count[v] -= 1 
            bucket[count[v]] = L[j]
        #收集数据
        L[:] = bucket[:] 


if __name__ == '__main__':
    L = [1,6,5,3,2,4]
    print('排序前：', L)
    radixSort(L, len(L), 10, 1)
    print('排序后：', L)