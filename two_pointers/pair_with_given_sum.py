# Given a sorted array of integers (not necessarily distinct) A and an integer B, find
# and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.
# Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = len(A) - 1
        mod = int(10 ** 9 + 7)
        ans = 0

        while i < j:
            if A[i] + A[j] == B:
                if A[i] == A[j]:
                    count = j - i + 1
                    ans += ((count * (count-1)) // 2 ) % mod
                    ans = ans % mod
                    break
                else:
                    ii, jj = i, j
                    # count number of elements with value A[i]
                    while A[i] == A[ii]:
                        ii += 1
                    count1 = ii - i
                    i = ii

                    # count number of elements with value A[j]
                    while A[j] == A[jj]:
                        jj -= 1
                    count2 = j - jj
                    j = jj
                    ans += count1 * count2
                    ans = ans % mod
            elif A[i] + A[j] < B:
                i += 1
            else:
                j -= 1

        return ans



if __name__ == '__main__':
    a = [2, 2, 3, 4, 4, 5, 6, 7, 10]
    b = 8
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')