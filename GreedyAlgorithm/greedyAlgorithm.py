#=======================贪心算法========================
'''
贪婪算法可以获取到问题的局部最优解，不一定能获取到全局最优解
简单同时还能得到比较不错的结果的算法（非常切合中庸之道)
'''

#=======================0/1背包问题========================

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

# 定义三种策略
def value(item):
    return item.getValue()
def weightInverse(item):
    return 1.0/item.getWeight()
def density(item):
    return item.getValue() / item.getWeight()

def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
        if totalWeight + itemsCopy[i].getWeight() <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result,totalValue)

# 测试
def buildItems():
    names = ['A','B','C','D','E','F','G']
    weights = [10,40,30,50,35,40,30]
    values = [35,30,6,50,40,10,25]
    Items = []
    for i in range(len(names)):
        Items.append(Item(names[i],weights[i],values[i]))
    return Items

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('total value:', val)
    for item in taken:
        print(' ', item)

def testGreedys(maxWeight = 150):
    items = buildItems()
    print('maxWeight is ', maxWeight)

    print('use greedy by value...')
    testGreedy(items, maxWeight, value)

    print('use greedy by weight...')
    testGreedy(items, maxWeight, weightInverse)

    print('use greeedy by density')
    testGreedy(items, maxWeight, density)


if __name__ == '__main__':
    start = time.clock()
    testGreedys()
    end = time.clock()
    print('time: ', end-start)