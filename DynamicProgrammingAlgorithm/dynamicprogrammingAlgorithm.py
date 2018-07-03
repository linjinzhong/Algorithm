#=======================动态规划========================
'''
解决一类最优化问题，具有重复子问题和最优子结构的问题。
将一个复杂的问题分解成若干个子问题，通过综合子问题的最优解得到原问题的最优解。
动态规划会将每个子问题的解记录下来，这样当下次遇到同样子问题时，就可以直接使用之前的记录无须重复计算。
如果一个问题的最优解可以由它的子问题的最优解有效的构造和处理，称这个问题拥有最优子结构。
一个问题必须拥有重叠子问题和最优子结构才能使用动态规划去解决。

动态规划是自底向上，要等待子问题求解完毕，记录子问题的解，综合选择最佳的一个。
动态规划要看哪个选择笑到最后，暂时的领先说明不了什么。
动态规划快在记录子问题的解。
'''

#=======================0/1背包问题=====================

import time

class Item(object):
    def __init__(self,n,w,v):
        self.name = n
        self.weight = float(w)
        self.value = float(v)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ',' + str(self.value) + ',' + str(self.weight) + '>'
        return result

def buildItems():
    names = ['A','B','C','D','E','F','G']
    weights = [10,40,30,50,35,40,30]
    values = [35,30,6,50,40,10,25]
    Items = []
    for i in range(len(names)):
        Items.append(Item(names[i],weights[i],values[i]))
    return Items

def findMaxVal(Items, leftRoom, memo={}):
    if (len(Items), leftRoom) in memo:
        #如果之前计算过
        result = memo[len(Items), leftRoom]
    elif Items == [] or leftRoom == 0:
        #Items为空或者背包剩余容量为0
        result = (0,())
    elif Items[0].getWeight() > leftRoom:
        #仅右子树
        result = findMaxVal(Items[1:],leftRoom,memo)
    else:
        curItem = Items[0]
        #取curItem,左子树
        leftValue, leftToken = findMaxVal(Items[1:], leftRoom-curItem.getWeight(), memo)
        leftValue += curItem.getValue()
        #不取curItem,右子树
        rightValue, rightToken = findMaxVal(Items[1:], leftRoom, memo)

        if leftValue > rightValue:
            result = (leftValue, leftToken+(curItem,))
        else:
            result = (rightValue, rightToken)
    memo[len(Items), leftRoom] = result
    return result

def backpackbyDP():
    Items = buildItems()
    value,token = findMaxVal(Items, 150)
    for item in token:
        print(item)
    print('total valuse of tokens is: ', value)

if __name__ == '__main__':
    start = time.clock()
    backpackbyDP()
    end = time.clock()
    print('time: ', end-start)