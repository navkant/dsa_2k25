# Given the inorder and postorder traversal of a tree, construct the binary tree.
# NOTE: You may assume that duplicates do not exist in the tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, A, B):
        if not A or not B:
            return None
        
        root_val = B.pop()
        root_index = A.index(root_val)

        root = TreeNode(x=root_val)
        root.right = self.buildTree(A[root_index+1:], B)
        root.left = self.buildTree(A[:root_index], B)

        return root



if __name__ == "__main__":
    A = [6, 1, 3, 2]
    B = [6, 3, 2, 1]

    root = Solution().buildTree(A, B)
    breakpoint()