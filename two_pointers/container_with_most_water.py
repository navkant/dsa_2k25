# Given N non-negative integers A[0], A[1], ..., A[N-1] , where each represents a point at coordinate (i, A[i]).
#
# N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).
#
# Find two lines, which together with x-axis forms a container, such that the container contains the most water. You need to return this maximum area.
#
# Note: You may not slant the container. It is guaranteed that the answer will fit in integer limits.


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        i = 0
        j = len(A) - 1

        ans = 0

        while i < j:
            ans = max(ans, ((j - i) * min(A[i], A[j])))

            if A[i] < A[j]:
                i += 1
            else:
                j -= 1

        return ans


if __name__ == "__main__":
    a = [1, 5, 4, 3]
    obj = Solution()
    ans = obj.maxArea(a)
    print(f'ans is {ans}')






