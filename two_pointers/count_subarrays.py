# Misha likes finding all Subarrays of an Array. Now she gives you an array A of N elements and told you to find
# the number of subarrays of A, that have unique elements.
# Since the number of subarrays could be large, return value % 109 +7.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mod = 10 ** 9 + 7
        l = 0
        r = 0
        n = len(A)
        freq_map = {}
        # freq_map[A[0]] = 1
        count = 0

        while r < n and l <= r:
            if A[r] not in freq_map:
                freq_map[A[r]] = 1
            else:
                freq_map[A[r]] += 1

            if freq_map[A[r]] > 1:
                while freq_map[A[r]] > 1:
                    freq_map[A[l]] -= 1
                    l += 1
            else:
                pass

            count += r - l + 1
            r += 1

        return count % mod


if __name__ == '__main__':
    # a = [93, 9, 12, 32, 97, 75, 32, 77, 40, 79, 61, 42, 57, 19, 64, 16, 86, 47, 41, 67, 76, 63, 24, 10, 25,
    #      96, 1, 30, 73, 91, 70, 65, 53, 75, 5, 19, 65, 6, 96, 33, 73, 55, 4, 90, 72, 83, 54, 78, 67, 56, 8, 70, 43, 63]
    a = [1, 1, 3, 1]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')