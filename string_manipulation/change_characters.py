# You are given a string A of size N consisting of lowercase alphabets. You can change at most B characters in the given
# string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.
# Find the minimum number of distinct characters in the resulting string.


class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        arr = [0] * 26
        distinct_char = 0

        for char in A:
            arr[ord(char) - 97] += 1

        for freq in arr:
            if freq != 0:
                distinct_char += 1

        arr.sort()

        for index, freq in enumerate(arr):
            if freq != 0 and B - freq >= 0:
                distinct_char -= 1
                B -= freq

        return distinct_char


if __name__ == "__main__":
    obj = Solution()
    A = "abcabbccd"
    B = 3
    print(obj.solve(A, B))


