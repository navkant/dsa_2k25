class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        n = len(s)
        freq_map = {}
        input_string = s

        ans = ''
        max_length = 0

        while r < n:
            if input_string[r] not in freq_map:
                freq_map[input_string[r]] = 1
            else:
                freq_map[input_string[r]] += 1

            if freq_map[input_string[r]] > 1:
                while l <= r and freq_map[input_string[r]] > 1:
                    freq_map[input_string[l]] -= 1
                    l += 1

            if r - l + 1 > max_length:
                ans = input_string[l:r + 1]
                max_length = r - l + 1
            else:
                pass

            r += 1

        return max_length


if __name__ == "__main__":
    input = "abcabcbb"
    obj = Solution()
    print(obj.lengthOfLongestSubstring(input))