#=======================最长不下降子序列(LIS)===========================
#==================Longest Increasing Subsequence=====================
#可以不连续
#dp[i]表示第i位结尾的不下降子序列的长度
def LIS(L):
    dp = [0]*len(L)
    for i in range(0,len(L)):
        dp[i] = 1               #边界,每个元素自成一个序列
        for j in range(0,i):    #b遍历i之前的元素L[1~i-1]
            if L[i] >= L[j] and dp[j]+1>dp[i]:
                dp[i] = dp[j] + 1   #状态转移方程
    return max(dp)

if __name__ == '__main__':
    L = [3,18,7,14,10,12,23,41,16,24]
    print(LIS(L))