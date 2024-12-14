# You are given an integer array A denoting the Level Order Traversal of the Binary Tree.
# You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.
from collections import deque

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):
        dq = deque()
        root = TreeNode(A[0])
        dq.append(root)
        i = 1

        while dq:
            node = dq.popleft()
            if node == -1:
                continue

            if A[i] != -1:
                left_child = TreeNode(A[i])
                node.left = left_child
                dq.append(left_child)
            else:
                dq.append(-1)

            if A[i+1] != -1:
                right_child = TreeNode(A[i+1])
                node.right = right_child
                dq.append(right_child)
            else:
                dq.append(-1)

            i += 2

        return  root
