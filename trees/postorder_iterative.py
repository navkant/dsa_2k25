# Given a binary tree, return the preorder traversal of its nodes values.

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def __init__(self):
        self.stack = []
        self.inorder = []

    def postorderIterativeTraversal(self, A):
        node = A

        while node:
            self.stack.append(node)
            if node.left:
                node = node.left
            elif self.stack:
                while self.stack and self.stack[-1].right is None:
                    temp = self.stack.pop()
                if self.stack:
                    temp = self.stack.pop()
                    node = temp.right
                else:
                    break
            else:
                break
        return self.inorder


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
    print(obj.postorderIterativeTraversal(node1))

