# Given a binary tree, return a 2-D array with vertical order traversal of it.
# Go through the example and image for more details.
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
    def __init__(self):
        self.level_map = {}
    
    def verticalOrderTraversal(self, A):
        if A is None:
            return []
        
        queue = deque()
        h_index = 0
        queue.append((A, h_index))

        while queue:
            lvl_size = len(queue)

            for i in range(lvl_size):
                node, node_h_index = queue.popleft()

                if node_h_index not in self.level_map:
                    self.level_map[node_h_index] = [node.val]
                else:
                    self.level_map[node_h_index].append(node.val)
                
                if node.left:
                    queue.append((node.left, node_h_index - 1))
                if node.right:
                    queue.append((node.right, node_h_index + 1))
        
        ans = []
        for key in sorted(self.level_map.keys()):
            ans.append(self.level_map[key])

        return ans


if __name__ == "__main__":
    #            (1)
    #         /       \
    #       (2)       (3)
    #      /  \      /   \
    #   (4)   (0)  (5)   (6)
    #              /     /  \
    #           (7)    (8)   (9)

    node1 = TreeNode(460)
    node2 = TreeNode(3871)
    node3 = TreeNode(4698)
    node4 = TreeNode(8399)
    node5 = TreeNode(504)
    node6 = TreeNode(4421)
    node7 = TreeNode(7515)
    node8 = TreeNode(4167)
    node9 = TreeNode(5727)
    node10 = TreeNode(3096)
    node11 = TreeNode(434)
    node12 = TreeNode(7389)
    node13 = TreeNode(267)
    node14 = TreeNode(5661)
    node15 = TreeNode(4292)
    node16 = TreeNode(3006)
    node17 = TreeNode(6906)
    node18 = TreeNode(1969)
    node19 = TreeNode(7815)
    node20 = TreeNode(9750)
    node21 = TreeNode(6693)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.right = node8
    node5.left = node9
    node6.right = node10
    node7.left = node11
    node7.right = node12



    node8.left = node13
    node8.right = node14
    node9.left = node18
    node9.right =node19
    node10.left = node15
    node10.right = node16
    node11.left = node20
    node11.right = node21
    node12.right = node17



    obj = Solution()
    print(obj.verticalOrderTraversal(node1))