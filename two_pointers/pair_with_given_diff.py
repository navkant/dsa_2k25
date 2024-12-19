# Given an one-dimensional integer array A of size N and an integer B.
# Count all distinct pairs with difference equal to B.
# Here a pair is defined as an integer pair (x, y), where x and y are
# both numbers in the array and their absolute difference is B.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hash_map = {}
        count = 0

        for i in range(len(A)):
            if A[i] not in hash_map:
                hash_map[A[i]] = 1
            else:
                hash_map[A[i]] += 1

        for k in hash_map.keys():
            if B == 0:
                if hash_map[k] > 1:
                    count += 1

            if B + k in hash_map:
                count += 1

        return count


if __name__ == "__main__":
    a = [8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3]
    b = 3
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
