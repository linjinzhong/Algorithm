#=======================最大连续子序列和(MCSS)===========================
#=================Maximum Continuous Subsequence Sum======================
#返回最大值
def MCSS_V1(L):
    dp = [0]*len(L) #dp[i]存放以A[i]结尾的最大连续子序列和
    dp[0] = L[0]    #边界
    for i in range(1,len(L)):
        #状态转移方程
        dp[i] = max(L[i], dp[i-1]+L[i])
    return max(dp)

#返回最大值和相应序列index
def MCSS_V2(L):
    dp = [0]*len(L) #dp[i]存放以A[i]结尾的最大连续子序列和
    dp[0] = L[0]    #边界
    curIndex = [0]
    maxV = L[0]
    maxIndex = [0]
    for i in range(1,len(L)):
        #状态转移方程
        if L[i] > dp[i-1] + L[i]:
            dp[i] = L[i]
            curIndex = [i]
        else:
            dp[i] = dp[i-1] + L[i]
            curIndex += [i]
        if dp[i] > maxV:
            maxV = dp[i]
            maxIndex[:] = curIndex[:]
    return maxV, maxIndex

if __name__ == '__main__':
    L = [-2, 11, -4, 13, -5, -2]
    # print(MCS_V1(L))
    val, index = MCSS_V2(L)
    print(val, index)