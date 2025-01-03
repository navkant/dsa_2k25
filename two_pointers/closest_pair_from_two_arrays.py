# Given two sorted arrays of distinct integers, A and B, and an integer C, find and return the pair whose sum 
# is closest to C and the pair has one element from each array.
# More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value.
# If there are multiple solutions find the one with minimum i and even if there are multiple values of j for the same i then return the one with minimum j.
# Return an array with two elements {A[i], B[j]}.

import sys

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(A)
        m = len(B)
        l = 0
        r = m - 1

        diff = sys.maxsize
        ans = [-1, -1]
        ind = [-1, -1]

        while l < n and r >= 0:
            summ = A[l]  + B[r]
            x = abs(summ - C)

            if x < diff:
                diff = x
                ans = [A[l], B[r]]
                ind = [l, r]
            elif x == diff:
                if l == ind[0]:
                    ans = [A[l], B[r]]
                    ind = [l, r]
            
            if summ > C:
                r -= 1
            else:
                l += 1
        
        return ans





if __name__ == "__main__":
    a = [1]
    b = [2, 4]
    c = 4
    obj = Solution()
    ans = obj.solve(a, b, c)
    print(f'ans is {ans}')