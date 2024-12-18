# Given a binary tree, Populate each next pointer to point to its next right node. If there is no next right
# node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL. Assume perfect binary tree.
from collections import deque


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return nothing

    def connect(self, root):
        dq = deque()
        dq.append(root)

        while dq:
            lvl_size = len(dq)

            start = dq.popleft()
            if start.left:
                dq.append(start.left)
            if start.right:
                dq.append(start.right)


            for i in range(1, lvl_size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

                start.next = node
                start = node







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
    print(obj.connect(node1))
