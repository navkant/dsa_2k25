# Given a root of binary tree A, determine if it is height-balanced. A height-balanced binary tree is defined
# as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.is_balanced = 1
    def is_tree_balanced(self, node: TreeNode):
        if node is None:
            return -1

        height_left_subtree = self.is_tree_balanced(node.left) + 1
        height_right_subtree = self.is_tree_balanced(node.right) + 1

        if abs(height_left_subtree - height_right_subtree) > 1:
            self.is_balanced = 0

        return max(height_left_subtree, height_right_subtree)

    def isBalanced(self, A):
        self.is_tree_balanced(A)
        return self.is_balanced


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
    node10 = TreeNode(0)

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
    print(obj.isBalanced(node1))
