#=========================二叉查找树===========================

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def __init__(self, data):
        self.root = TreeNode(data[0])
        for d in data[1:]:
            self.insert(self.root, d)

    # 查找
    def search(self, root, x):
        if not root:
            print(x, 'is not found!')
            return None
        if x < root.val:
            return self.search(root.left, x)
        elif x > root.val:
            return self.search(root.right, x)
        else:
            print(x, 'is found!')
            return root

    # 插入
    def insert(self, root, x):
        if not root:
            root = TreeNode(x)
            # print('successful inset ', x)
        else:
            if x < root.val:
                root.left = self.insert(root.left, x)
            elif x > root.val:
                root.right = self.insert(root.right, x)
            else:
                print('is already in tree!')
        return root

    # 找前驱中最大点
    def findPreMax(self, root):
        while root.right:
            root = root.right
        return root

    # 找后继中最小点
    def findPostMin(self, root):
        while root.left:
            root = root.left
        return root

    # 删除
    def delete(self, root, x):
        if not root:
            print(x, 'is not found in tree')
        elif x < root.val:
            root.left = self.delete(root.left, x)
        elif x > root.val:
            root.right = self.delete(root.right, x)
        elif root.left and root.right:
            right_min = self.findPostMin(root.right)
            root.val = right_min.val
            root.right = self.delete(root.right, right_min.val)
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = None
        return root


    # 前序遍历
    def preOrderTraverse(self, root):
        if root:
            print(root.val)
            self.preOrderTraverse(root.left)
            self.preOrderTraverse(root.right)
    # 中序遍历
    def inOrderTraverse(self, root):
        if root:
            self.inOrderTraverse(root.left)
            print(root.val)
            self.inOrderTraverse(root.right)
    # 后序遍历
    def postOrderTraverse(self, root):
        if root:
            self.postOrderTraverse(root.left)
            self.postOrderTraverse(root.right)
            print(root.val)

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
    data = [8,3,9,1,6,2,5,7]
    #创建二叉搜索树
    bst = BST(data)
    #查找
    bst.search(bst.root, 3)
    #插入
    bst.insert(bst.root, 4)
    #删除
    bst.delete(bst.root, 3)
    #层序遍历
    bst.layerOrderTraverse(bst.root)



