# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
# adding up all the values along the path equals the given sum.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = 0

    def check_has_path_sum(self, node, summ, key):
        if node is None:
            if summ == key:
                self.ans = 1
            return

        self.check_has_path_sum(node.left, summ + node.val, key)
        self.check_has_path_sum(node.right, summ + node.val, key)

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        self.check_has_path_sum(A, summ=0, key=B)
        return self.ans

if __name__ == "__main__":
    #            (1)
    #         /       \
    #       (2)       (3)
    #      /  \      /   \
    #   (4)   (0)  (5)   (6)
    #              /     /  \
    #           (7)    (8)   (9)

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node10
    node3.left = node5
    node3.right = node6
    node5.left = node7
    node6.left = node8
    node6.right = node9

    obj = Solution()
    print(obj.hasPathSum(node1, 3))
