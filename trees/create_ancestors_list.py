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
        self.ans = []
        self.ancestor_list = []

    def create_ancestor_list(self, node: TreeNode, key: int):
        # print(self.ancestor_list)
        if node is None:
            return

        self.ancestor_list.append(node.val)
        self.create_ancestor_list(node.left, key)
        self.create_ancestor_list(node.right, key)

        if node.val == key:
            self.ans = self.ancestor_list[:]
        else:
            self.ancestor_list.pop()

    def solve(self, node: TreeNode, key: int):
        self.create_ancestor_list(node, key)
        return self.ans


if __name__ == "__main__":
    #            (1)
    #         /       \
    #       (2)       (3)
    #      /  \      /   \
    #   (4)   (10)  (5)   (6)
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
    key = 9
    print(obj.solve(node1, key))
