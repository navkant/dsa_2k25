# Given a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def __init__(self):
        self.inorder_list = []
    
    def inorder_traversal(self, node: TreeNode):
        if node is None:
            return
        
        self.inorder_traversal(node.left)
        self.inorder_list.append(node.val)
        self.inorder_traversal(node.right)

        

    
    def inorderTraversal(self, A):
        self.inorder_traversal(A)
        return self.inorder_list

    
if __name__ == "__main__":
    # [4, 2, 0, 1, 7, 5, 3, 8, 6, 9]
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
    print(obj.inorderTraversal(node1))

        



