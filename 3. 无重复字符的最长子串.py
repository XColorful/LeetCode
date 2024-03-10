# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长
# 子串
#  的长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_num = 0
        long_str = ""
        for add_str in s: # 对字符串的每一位依次添加
            long_str += add_str
            for i in range(0, len(long_str) - 1): # 除了最后一项刚添加的
                if add_str == long_str[i]:
                    long_str = long_str[i+1:]
                    break
            new_len = len(long_str)
            if new_len > long_num:
                long_num = new_len
        return long_num

a = Solution()
s = "abcb"
print(a.lengthOfLongestSubstring(s))