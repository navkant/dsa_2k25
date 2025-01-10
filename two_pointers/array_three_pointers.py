import sys


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        x = len(A)
        y = len(B)
        z = len(C)
        i = j = k = 0

        diff = 99999999

        while i < x and j < y and k < z:
            minn = min(A[i], B[j], C[k])
            maxx = max(A[i], B[j], C[k])
            diff = min(diff, maxx - minn)

            if minn == A[i]:
                i += 1
            elif minn == B[j]:
                j += 1
            elif minn == C[k]:
                k += 1

        return diff


if __name__ == "__main__":
    a = [3, 5, 6]
    b = [2]
    c = [3, 4]
    obj = Solution()
    ans = obj.minimize(a, b, c)
    print(f'ans is {ans}')
