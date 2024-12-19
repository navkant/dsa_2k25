# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
# If the answer does not exist return an array with a single integer "-1".
# First sub-array means the sub-array for which starting index in minimum.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        i = 0
        j = 1
        temp_sum = A[0]

        while j < n:
            temp_sum += A[j]

            if temp_sum == B:
                return A[i: j+1]
            elif temp_sum < B:
                pass
            else:
                while i < j and temp_sum > B:
                    temp_sum -= A[i]
                    i += 1
                    if temp_sum == B:
                        return A[i: j+1]
            j += 1

        return [-1]


if __name__ == "__main__":
    a = [5, 10, 20, 100, 105]
    b = 110
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
