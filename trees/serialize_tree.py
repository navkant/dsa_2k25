# Given the root node of a Binary Tree denoted by A. You have to Serialize the given Binary Tree in the described format.
# Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.
from collections import deque


class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers

    def solve(self, A):
        dq = deque()
        dq.append(A)
        ans = []
        while dq:
            lvl_size = len(dq)
            lvl_array = []
            for i in range(lvl_size):
                node = dq.popleft()
                if node != -1:
                    lvl_array.append(node.val)
                    if node.left:
                        dq.append(node.left)
                    else:
                        dq.append(-1)

                    if node.right:
                        dq.append(node.right)
                    else:
                        dq.append(-1)
                else:
                    lvl_array.append(node)
            ans += lvl_array

        return ans


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
    print(obj.solve(node1))
