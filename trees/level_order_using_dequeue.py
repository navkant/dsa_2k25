# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class DeQueue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
        self.end += 1
    
    def dequeue(self):
        self.start += 1
        return self.queue[self.start]
    
    def is_empty(self):
        if self.start == self.end:
            return True
        else:
            return False
    
    def get_size(self):
        return self.end - self.start


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        dq = DeQueue()
        dq.enqueue(A)
        ans = []

        while not dq.is_empty():
            level_array = []
            level_size = dq.get_size()

            for i in range(level_size):
                element = dq.dequeue()
                level_array.append(element.val)

                if element.left:
                    dq.enqueue(element.left)
                
                if element.right:
                    dq.enqueue(element.right)
            ans.append(level_array)
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
