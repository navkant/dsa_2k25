# Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the
# array. The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both
# S1 and S2. Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
import sys


class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        min_length = sys.maxsize

        for string in A:
            if len(string) < min_length:
                min_length = len(string)

        common_prefix = ""

        for i in range(min_length):
            char = A[0][i]
            count = 0
            for j in range(len(A)):
                if A[j][i] == char:
                    count += 1
            if count == len(A):
                common_prefix += char

        print(common_prefix)



if __name__ == "__main__":
    a = ["abcdefgh", "aefghijk", "abcefgh"]
    print(a)
    obj = Solution()
    ans = obj.longestCommonPrefix(a)
    print('ans is: ', ans)