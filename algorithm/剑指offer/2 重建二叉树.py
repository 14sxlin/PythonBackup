class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(root, order):
    if root is not None:
        order.append(root.value)
        preorder(root.left, order)
        preorder(root.right, order)


def inorder(root, order):
    if root is not None:
        inorder(root.left,order)
        order.append(root.value)
        inorder(root.right,order)


if __name__ == '__main__':

    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]


    def reConstructBinaryTree(preSubTree, inSubTree):
        """
        :param preSubTree: 子树的先序遍历
        :param inSubTree:  子树的中序遍历
        :return:
        """
        if len(preSubTree) != len(inSubTree):
            print("wrong tree")
            return
        if len(preSubTree) == 0:
            return None
        node = TreeNode(preSubTree[0])
        index = inSubTree.index(node.value)
        leftSubTreeLen = index + 1  # 找到遍历中对应的子树部分,进入下一次迭代
        node.left = reConstructBinaryTree(preSubTree[1:leftSubTreeLen], inSubTree[:index])
        node.right = reConstructBinaryTree(preSubTree[leftSubTreeLen:], inSubTree[index + 1:])
        return node


    root = reConstructBinaryTree(pre_order, in_order)
    preList = []
    preorder(root, preList)
    inList = []
    inorder(root, inList)
    assert preList == pre_order
    assert inList == in_order
    print("success")
