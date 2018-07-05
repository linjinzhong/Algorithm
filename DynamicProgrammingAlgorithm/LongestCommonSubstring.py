#=======================最长公共子串(LCSstr)===========================
#=====================Longest Common Substring========================
# A[...i...] len(A) = N
# B[...j...] len(B) = M
# dp[i,j]:表示A[...i-1]和B[...j-1]的最长公共子序列, 维度为(N+1)x(M+1)
# 边界：第0行和第0列为0，只要全部初始化为0即可
#           |--> 0                            若 i=0 或 j=0
# dp[i,j] = |--> dp[i-1][j-1]+1               若 i,j>0, x_i = y_j
#           |--> max{dp[i-1][j], dp[i][j-1]}  若 i,j>0, x_i /= y_j

def LCSstr(A,B):
    N, M = len(A), len(B)
    maxV, x, y = -1, -1, -1
    for i in range(1,N+1):
        for j in range(1,M+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                pre[i][j] = 0   #代表前一个结点在左上方
            else:
                dp[i][j] = 0
            if dp[i][j] > maxV:
                maxV = dp[i][j]
                x, y = i, j
    return maxV, x, y

def subString(x, y):
    str = []
    while x > -1 and y > -1:
        if A[x-1] == B[y-1]:
            str = [A[x-1]] + str
            x, y = x - 1, y - 1
        else:
            break
    return str


if __name__ == '__main__':
    A = ['B','D','C','A','B','A']
    B = ['A','B','C','B','D','A','B']
    N, M = len(A), len(B)
    dp = [[0]*(M+1) for i in range(N+1)]
    pre = [[0]*(M+1) for i in range(N+1)]
    maxV, x, y = LCSstr(A,B)
    print(maxV, (x,y))
    print(subString(x,y))
