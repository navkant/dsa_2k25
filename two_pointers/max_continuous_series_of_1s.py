# Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B zeroes.
# For this problem, return the indices of maximum continuous series of 1s in order.
# If there are multiple possible solutions, return the sequence which has the minimum start index.


class Solution:
    def maxone(self, A, B):
        pass
        


if __name__ == '__main__':
    a = [1, 0, 0, 0, 1, 0, 1]
    b = 2
    obj = Solution()
    ans = obj.maxone(a, b)
    print(f'ans is {ans}')