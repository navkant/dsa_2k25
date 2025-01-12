# Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B zeroes.
# For this problem, return the indices of maximum continuous series of 1s in order.
# If there are multiple possible solutions, return the sequence which has the minimum start index.


class Solution:
    def maxone(self, A, B):
        n = len(A)
        l = r = 0
        zero_count = 0
        ans = 0

        while r < n:
            if A[r] == 1:
                r += 1
            else:
                if zero_count < B:
                    zero_count += 1
                    r += 1
                else:
                    while l <= r and zero_count >= B:
                        if A[l] == 1:
                            pass
                        else:
                            zero_count -= 1
                        l += 1

            ans = max(ans, r - l)

        return ans


if __name__ == '__main__':
    a = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    b = 1
    obj = Solution()
    ans = obj.maxone(a, b)
    print(f'ans is {ans}')