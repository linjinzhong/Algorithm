#=======================最长回文子串(LCSstr)===========================
#=====================Longest Palindrome Substring========================
# 边界：每个字符本身是一个回文子串，连续两个相同字符为回文子串
# 状态转移方程：枚举子串长度3~len
#   如果子串左右端点相同并且左端点右边一个端点和右端点左边一个节点组成的子串
#       为回文串，则新子串也为回文串。

def LPS(S):
    N = len(S)
    dp = [[0]*N for i in range(N)]
    start, ans = 0, 1   #最长回文串起点和长度
    #初始化边界
    for i in range(N):
        dp[i][i] = 1
        if i < N-1:
            if S[i] == S[i+1]:
                dp[i][i+1] = 1
                start = i
                ans = 2
    #状态转移
    for L in range(3,N+1):  #枚举子串长度
        for i in range(N+1-L): #枚举子串起点
            j = i + L -1    #子串右端点
            if S[i] == S[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1
                start = i   #更新起点
                ans = L     #更新回文子串长度

    return S[start:start+ans]
    


if __name__ == '__main__':
    S = 'abcddeddfgh'
    print(LPS(S))
