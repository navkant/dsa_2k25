# Given an array A of N integers, find three integers in A such that the sum is closest to
# a given number B. Return the sum of those three integers.
# Assume that there will only be one solution.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        n = len(A)
        minDiff = 2147483648
        ret = 0
        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                temp = A[i] + A[j] + A[k]
                diff = abs(temp - B)
                if diff == 0:
                    return temp
                if diff < minDiff:
                    minDiff = diff
                    ret = temp
                if temp <= B:
                    j += 1
                else:
                    k -= 1
        return ret


if __name__ == "__main__":
    pass
