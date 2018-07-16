#=========================平衡二叉树===========================
# AVL树是带有平衡条件的二叉查找树，
# 一般要求每个节点的左子树和右子树的高度最多差1(空树的高度定义为-1)。
# 在高度为h的AVL树中，最少的节点数S(h)由S(h)=S(h-1)+S(h-2)+1得出，
# 其中S(0)=1，S(1)=2。

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

class AVLTree(object):
    # def __init__(self):
    #     self.root = None
    def __init__(self, data):
        self.root = TreeNode(data[0])
        for d in data[1:]:
            self.root = self.insert(self.root, d)
    def find(self, node, val):
        if node is None:
            return None
        elif val < node.val:
            return self.find(node.left, val)
        elif val > node.val:
            return self.find(node.right, val)
        else:
            print(node.val, 'is found!')
            return node

    def findMin(self, node):
        if node.left:
            return self.findMin(node.left)
        else:
            return node

    def findMax(self, node):
        if node.right:
            return self.findMax(node.right)
        else:
            return node

    def height(self, node):
        if node is None:
            return -1
        else: 
            return node.height

    # 插入
    # 插入一个节点后，只有从插入节点到根节点的路径上的节点的平衡可能被改变。
    # 我们需要找出第一个破坏了平衡条件的节点，称之为K。K的两颗子树的高度差2.
    # 不平衡有四种情况:
        # 1.对K的左儿子的左子树进行一次插入
        # 2.对K的左儿子的右子树进行一次插入
        # 3.对K的右儿子的左子树进行一次插入
        # 4.对K的右儿子的右子树进行一次插入
    # 情况1与4是对称的，需要进行一次单旋转操作，
    # 清况2与3需要一次双旋转操作。
    #LL
    def LL(self, node):
        k = node.left
        node.left = k.right
        k.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k.height = max(self.height(k.left), node.height) + 1
        return k
    #RR
    def RR(self, node):
        k = node.right
        node.right = k.left
        k.left = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        k.height = max(self.height(k.right), node.height) + 1
        return k
    # LR
    def LR(self, node):
        node.left = self.RR(node.left)
        return self.LL(node)       
    # RL
    def RL(self, node):
        node.right = self.LL(node.right)
        return self.RR(node)

    # 插入
    def insert(self, node, val):
        if node is None:
            node = TreeNode(val)
        elif val < node.val:
            node.left = self.insert(node.left, val)
            if self.height(node.left) - self.height(node.right) == 2:
                if val < node.left.val:
                    node = self.LL(node)
                else:
                    node = self.LR(node)
        elif val > node.val:
            node.right = self.insert(node.right, val)
            if self.height(node.right) - self.height(node.left) == 2:
                if val < node.right.val:
                    node = self.RL(node)
                else:
                    node = self.RR(node)
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    # 删除
    def delete(self, node, val):
        if node is node:
            print(val, 'is not found!')
        elif val < node.val:
            node.left = self.delete(node.left, val)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.RR(node)
                else:
                    node = self.RL(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        elif val > node.val:
            node.right = self.delete(node.right, val)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) > self.height(node.left.right):
                    node = self.LL(node)
                else:
                    node = self.LR(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        
        #删除当前node，其左右是否有子树
        elif node.left and node.right:
            # 若左右子树均存在,且右子树更高
            if node.left.height <= node.right.height:
                minNode = self.findMin(node.right)
                node.val = minNode.val
                node.right = self.delete(node.right, minNode.val)
            # 若左右子树均存在,且右子树更高
            else:
                maxNode = self.findMax(node.left)
                node.val = maxNode.val
                node.left = self.delete(node.left, maxNode.val)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        #删除当前node，其左or右有子树 
        else:
            if node.right:
                node = node.right
            else:
                node = node.left
        return node
        #层序遍历
    def layerOrderTraverse(self, root):
        L = [root]
        while L:
            node = L.pop(0)
            if node.left:
                L.append(node.left)
            if node.right:
                L.append(node.right)
            print(node.val)


if __name__ == '__main__':
    PRE = '1234567'
    IN = '3241657'
    POST = '3426751'
    LAYER = '1253467'

    AVL = AVLTree('1234567')
    AVL.layerOrderTraverse(AVL.root)

