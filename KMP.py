#=======================KMP===========================
#KMP算法，判断模式串是否是主串的子串
#KMP算法的每趟比较过程让子串向后滑动一个合适的位置，让这个位置上的字符和主串中的字符比较
#这个合适的位置与子串本身的结构有关。
#S(0),S(1),S(2),...,S(i-j),S(i-j+1),...,S(i-1),     S(i),   S(i+1),...,S(n-1)
#                         T(0),T(1),...,T(j-1),     T(j),    ...,T(m-1)
#S和T部分匹配成功恰好到S(i)和S(j)的时候匹配失败，。此时，有一下两种操作：
#   1）S(i-j+1)和T(0)重新比，即S往右移一位
#   2）T中寻找一个最大K位置，使得S(i-k),...,S(i-1)和T(0),...,T(k-1)匹配，当前待比较S(i)和T(k)。
#上述k可以根据模式串T求得
# 初始化:next[0] = -1,标记;
# 后面求解[1,N-1]位置上的next值;
# for j = 1,...,N-1:
#       要求next[j]的值，即求j位置不相等时，下一个待匹配的位置k;
#       假设k位置存在，只要判断[...,j-1]与[...,k-1]是否匹配，此时问题转换成待匹配位置为j-1和k-1,如此这般不断向前寻找。



def getNext(S):
    N = len(S)
    next = [-1]*N
    next[0] = -1    #
    for j in range(1,N):
        k = next[j-1] #取当前位置的前一个位置的待匹配值next[j-1]
        while k != -1 and S[j-1] != S[k]:   #如果k位置上的值与S[j-1]不等，继续回退k,直到相等或者K=-1标记处
            k = next[k]
        if S[j-1] == S[k]:
            next[j] = k+1
        else:
            next[j] = 0 #回退到-1标记处，说明该位置之前无法继续匹配，只有重新从首位开始匹配
    return next

# 返回匹配初始位置，未匹配则返回-1
def KMP(S, T, next, pos):
    #利用模式串T的next串值求T在主串S中第pos个字符之后的位置的KMP算法，其中0<=pos<len(S)
    i, j, N, M = pos, 0, len(S), len(T)
    while i < N and j < M:
        if j == -1 or S[i] == T[j]:
            i, j = i+1, j+1 #主模两串都往右移
        else:
            j = next[j]
        if j == M:
            return i-j  #找到一个即返回起始匹配位置

    return -1           #没找到则返回-1

#返回匹配个数，以及相应匹配初始位置
def KMP_N(S, T, next, pos):
    cnt = 0
    startList = []
    #利用模式串T的next串值求T在主串S中第pos个字符之后的位置的KMP算法，其中0<=pos<len(S)
    i, j, N, M = pos, 0, len(S), len(T)
    while i < N and j < M:
        if j == -1 or S[i] == T[j]:
            i, j = i+1, j+1 #主模两串都往右移
        else:
            j = next[j]
        if j == M:
            startList += [i-j]
            cnt += 1
            j = next[j-1]     #找到一个，因为最后找到是i和j都右移一位，所以要回退一位，同时j回退到next[j]继续匹配
            i -= 1

            
    return cnt, startList


if __name__ == '__main__':
    # S = 'abcabaaabaabcac'
    # T = 'abaabcac'
    #    #'-10011201'
    # next = getNext(T)
    # print('next: ',next)
    # pos = KMP(S,T,next,0);
    # print('起始匹配位置为：',pos)

    S = 'abaabbaabbaadd'
    T = 'aabbaa'
      #'-101001'
    next = getNext(T)
    print('next: ',next)
    cnt, L = KMP_N(S, T, next, 0)
    print(cnt, L)
