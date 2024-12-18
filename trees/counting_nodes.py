# Given the root of a tree A with each node having a certain value, find the count of nodes with more value than all its ancestors.
# Ancestor means that every node that occurs before the current node in the path from root to the node.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def count_nodes(self, node, max_so_far):
        if node is None:
            return 0

        if node.val > max_so_far:
            self.count += 1
            max_so_far = node.val

        self.count_nodes(node.left, max_so_far)
        self.count_nodes(node.right, max_so_far)


    # @param root, a tree node
    # @return nothing
    def solve(self, root):
        self.count_nodes(root, max_so_far=0)
        return self.count


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
    print(obj.solve(node1))
