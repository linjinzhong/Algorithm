#=========================重建树===========================

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#=============== 通过先序遍历序列和中序遍历序列=================
#根节点在先序遍历序列的左边第一个。
#根节点位于中序遍历序列的中间，并以此分为左右两子树。
#先找到先序遍历第一个元素在中序遍历中的位置，以此位置为分界。
#中序遍历中该位置左侧为左子树，右侧为右子树。
#不断递归创建。
def createTreeByPreIn(preL, preR, inL, inR):
    if preL > preR:
        return None
    root = TreeNode(PRE[preL])
    k = inL
    while IN[k] != PRE[preL]:
        k += 1
    nLeft = k - inL #左子树结点个数个数
    root.left = createTreeByPreIn(preL+1, preL+nLeft, inL, k-1)
    root.right = createTreeByPreIn(preL+nLeft+1, preR, k+1, inR)
    return root


#=============== 通过后序遍历序列和中序遍历序列=================
#根节点在后序遍历序列的最后一个。
#根节点位于中序遍历序列的中间，并以此分为左右两子树。
#先找到后序遍历最后一个元素在中序遍历中的位置，以此位置为分界。
#中序遍历中该位置左侧为左子树，右侧为右子树。
#不断递归创建。
def createTreeByPostIn(postL, postR, inL, inR):
    if postL > postR:
        return None
    root = TreeNode(POST[postR])
    k = inL
    while IN[k] != POST[postR]:
        k += 1
    nLeft = k - inL #左子树结点个数个数
    root.left = createTreeByPostIn(postL, postL+nLeft-1, inL, k-1)
    root.right = createTreeByPostIn(postL+nLeft, postR-1, k+1, inR)
    return root


#=============== 通过层序遍历序列和中序遍历序列=================
#层序遍历序列的从左到右结点以此为根节点。
#因此左右子结点递归时传入的层序遍历只能是当前层序遍历序列右移一位后所有元素。
#当前中序遍历中的某个根节点肯定在当前层序遍历序列中，
#只不过位置不确定，但是有先后顺序，即在层序遍历序列中，父结点肯定在子结点前面。
def createTreeByLayerIn(layerL, layerR, inL, inR):
    if inL > inR:
        return None
    k = inL
    # for k in range(inL, inR+1):      #切记这么写不行，因为k到不了inR+1
    #     if IN[k] == LAYER[layerL]:   #而C++for(k=inL,k<=inR,k++)中k有可能到inR+1
    #         break;                   #只有这样，后面k > inR判断才有意义
    while k <= inR:
        if IN[k] == LAYER[layerL]:
            break;
        k += 1
    if k > inR:
        return createTreeByLayerIn(layerL+1, layerR, inL, inR)
    else:
        root = TreeNode(LAYER[layerL])
        root.left = createTreeByLayerIn(layerL+1, layerR, inL, k-1)
        root.right = createTreeByLayerIn(layerL+1, layerR, k+1, inR)
        return root


def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


if __name__ == '__main__':
    PRE = '1234567'
    IN = '3241657'
    POST = '3426751'
    LAYER = '1253467'
    # root = createTreeByPreIn(0, len(PRE)-1, 0, len(IN)-1)
    # root = createTreeByPostIn(0, len(POST)-1, 0, len(IN)-1)
    root = createTreeByLayerIn(0, len(LAYER)-1, 0, len(IN)-1)
    printTree(root)

