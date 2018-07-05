#=======================最长公共子序列(LCSseq)==========================
#====================Longest Common Subsequence========================
# A[...i...] len(A) = N
# B[...j...] len(B) = M
# dp[i,j]:表示A[...i-1]和B[...j-1]的最长公共子序列, 维度为(N+1)x(M+1)
# 边界：第0行和第0列为0，只要全部初始化为0即可
#           |--> 0                            若 i=0 或 j=0
# dp[i,j] = |--> dp[i-1][j-1]+1               若 i,j>0, x_i = y_j
#           |--> max{dp[i-1][j], dp[i][j-1]}  若 i,j>0, x_i /= y_j

def LCSseq(A,B):
    for i in range(1,N+1):
        for j in range(1,M+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                pre[i][j] = 0   #代表前一个结点在左上方
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                    pre[i][j] = 1   #代表上方
                else:
                    dp[i][j] = dp[i][j-1]
                    pre[i][j] = -1  #左方
    return dp[N][M]

def subSequence(i, j, seq=[]):
    if i == 0 or j == 0:
        return
    if pre[i][j] == 0:
        #可以直接打印 print(B[j])
        seq += [B[j-1]]
        subSequence(i-1,j-1,seq)
    else:
        if pre[i][j] == 1:
            subSequence(i-1,j,seq)
        else:
            subSequence(i,j-1,seq)
    return seq[::-1]


if __name__ == '__main__':
    A = ['B','D','C','A','B','A']
    B = ['A','B','C','B','D','A','B']
    N, M = len(A), len(B)
    dp = [[0]*(M+1) for i in range(N+1)]
    pre = [[0]*(M+1) for i in range(N+1)]
    print(LCSseq(A,B))
    print(subSequence(N,M))
