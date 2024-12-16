# Given a binary tree, return the zigzag level order traversal of its nodes values.
# (ie, from left to right, then right to left for the next level and alternate between).

from collections import deque


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        if A is None:
            return []

        dq = deque()
        dq.append(A)
        ans = []

        while dq:
            level_array = []
            level_size = len(dq)

            for i in range(level_size):
                element = dq.popleft()
                level_array.append(element.val)

                if element.left:
                    dq.append(element.left)

                if element.right:
                    dq.append(element.right)
            ans.append(level_array)

        for i in range(1, len(ans), 2):
            ans[i] = ans[i][::-1]

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
