# Given a string A, rotate the string B times in clockwise direction and return the string.


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        n = len(A)
        for i in range(B):
            A = A[n-1] + A[:n-1]

        return A

if __name__ == "__main__":
    a = "hellodarling"
    b = 4
    obj = Solution()
    print(obj.solve(a, b))
