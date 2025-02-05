# Given a binary tree, return the level order traversal of its 
# nodes' values. (i.e., from left to right, level by level).


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def __init__(self):
        self.level_map = {}
    
    def level_order_traversal(self, node, level):
        if node is None:
            return
        
        if level not in self.level_map:
            self.level_map[level] = [node.val]
        else:
            self.level_map[level].append(node.val)

        self.level_order_traversal(node.left, level=level+1)
        self.level_order_traversal(node.right, level=level+1)
        

    def solve(self, A):
        self.level_order_traversal(A, 0)
        result_matrix = []

        for key, val in self.level_map.items():
            result_matrix.append(val)
        
        return result_matrix



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
