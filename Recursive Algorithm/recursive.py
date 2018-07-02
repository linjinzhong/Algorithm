#========================Fibonacci数列========================
#递归写法
def F(n):
    if n == 0 or n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

#改进
def F(n, dp):
    if n == 0 or n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = F(n-1, dp) + F(n-2, dp)
        return dp[n]

# if __name__ == '__main__':
#     maxV = 1000;
#     dp = [-1]*maxV
#     # print(F(5))
#     print(F(5,dp))



#========================全排列========================
def generateP(index):
    global n
    global P
    global hashTable
    if index == n + 1:
        print(P[1:])
        return
    for x in range(1, n+1): #枚举1-n位，试图将x填入p[index]
        if not hashTable[x]: #若x未使用
            P[index] = x #将x填入index位
            hashTable[x] = True #标记x为已使用
            generateP(index + 1) #处理第index+1
            hashTable[x] = False; #还原，即该index位上不使用x


# if __name__ == '__main__':
#     n = 3
#     P = [0]*(n+1)
#     hashTable = [False]*(n+1)
#     generateP(1)


#========================N皇后问题========================
'''
两两均不在同一行同一列同一对角线上,可基于全排列问题解决。
P的每一位代表不同行，P每一位上的数字代表不同列。全排列保证不再同行同列。
只要在全排列中搜索那些不在同一对角线的即是所求解。
'''
def generatePforQ(index):
    global n
    global P
    global cnt
    global hashTable
    if index == n + 1:
        #得到一个全排列，先标记为ture表示为所求正确排列
        flag = True
        #判断该排列是否含有对角线元素
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if abs(i-j) == abs(P[i]-P[j]):
                    flag = False
        if flag:
            #flag为True表示找到一种正确的全排列满足N皇后问题
            print(P)
            cnt += 1
        return
    for x in range(1,n+1):
        if not hashTable[x]:
            P[index] = x
            hashTable[x] = True
            generatePforQ(index+1)
            hashTable[x] = False

# 改进：递归到某一层由于一些事实不需要往下一个子问题递归
# 就可以直接返回上一层，叫做回溯法
def generatePforQBetter(index):
    global n
    global P
    global cnt
    global hashTable
    if index == n+1:
        # 递归边界,若能到达必是合法方案
        print(P)
        cnt += 1
        return
    #当前为index行
    for x in range(1,n+1):      #第x列
        if not hashTable[x]:    #第x列还没有皇后
            flag = True         #表示当前皇后不会和之前的皇后冲突
            for pre in range(1,index):    #遍历之前的皇后
                if abs(index-pre) == abs(x - P[pre]):
                    flag = False;
                    break;
            if flag:
                P[index] = x
                hashTable[x] = True
                generatePforQBetter(index+1)
                hashTable[x] = False



if __name__ == '__main__':
    n = 8
    P = [0]*(n+1)
    hashTable = [False]*(n+1)
    cnt = 0
    # generatePforQ(1)
    generatePforQBetter(1)
    print(cnt)