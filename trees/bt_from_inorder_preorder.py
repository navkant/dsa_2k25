# Given preorder and inorder traversal of a tree, construct the binary tree.
# NOTE: You may assume that duplicates do not exist in the tree.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, pre_order_rev, in_order):
        if not pre_order_rev or not in_order:
            return None

        root_val = pre_order_rev.pop()
        root_index = in_order.index(root_val)
        root = TreeNode(x=root_val)
        root.left = self.buildTree(pre_order_rev, in_order[:root_index])
        root.right = self.buildTree(pre_order_rev, in_order[root_index + 1:])

        return root


if __name__ == "__main__":
    preorder = [1, 2, 3]
    inorder = [2, 1, 3]

    root = Solution().buildTree(preorder[::-1], inorder)
    breakpoint()