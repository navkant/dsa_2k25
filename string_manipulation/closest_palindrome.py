# Groot has a profound love for palindrome which is why he keeps fooling around with strings.
# A palindrome string is one that reads the same backward as well as forward. Given a string A of size N consisting of
# lowercase alphabets, he wants to know if it is possible to make the given string a palindrome by changing exactly one
# of its character


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        mid = len(A) // 2
        mismatch_count = 0

        for i in range(mid):
            if A[i] == A[n - i - 1]:
                continue
            else:
                mismatch_count += 1

        if mismatch_count == 1:
            return "YES"
        elif mismatch_count > 1:
            return "NO"
        else:
            if n % 2 == 0:
                return "NO"
            else:
                return "YES"


if __name__ == "__main__":
    input = 'abdba'
    obj = Solution()
    print(obj.solve(input))