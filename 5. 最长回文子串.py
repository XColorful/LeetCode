# 给你一个字符串 s，找到 s 中最长的回文
# 子串
# 。

# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_left_right(s, index, adjust):
            # find(mid, num):
            # if mid-num == mid+num:
            # return find(mid, num+1)
            # return num
            left_index = int(index - adjust)
            right_index = int(index + adjust)
            if left_index < 0 or right_index >= len(s):
                return adjust - 1
            if s[left_index] == s[right_index]: # 左右n位相等
                return find_left_right(s, index, adjust + 1) # 尝试左右n+1位
            else:
                return adjust - 1
        index = 0
        max_adjust = 0
        s_len = len(s)
        for i in range(s_len):
            if i+1 < s_len:
                if s[i+1] == s[i]: # 中心为双数
                    adjust = find_left_right(s, i+0.5, 0.5)
                    if adjust > max_adjust:
                        index = i+0.5
                        max_adjust = adjust
                if s[i+1] == s[i-1]: # 中心为单数，索引-1为相同char
                    adjust = find_left_right(s, i, 0)
                    if adjust > max_adjust:
                        index = i
                        max_adjust = adjust
        return s[int(index - max_adjust): int(index +1 + max_adjust)]

a = Solution()
s = "cbbd"
print(a.longestPalindrome(s))


class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/longest-palindromic-substring/solutions/255195/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 看答案方案二（同思路）改良后解法，速度提升
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_left_right(s, index, adjust):
            # find(mid, num):
            # if mid-num == mid+num:
            # return find(mid, num+1)
            # return num
            left_index = int(index - adjust)
            right_index = int(index + adjust)
            while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
                adjust += 1 # 可能是小数，但不要紧
                left_index -= 1 #已经是整数，不用套int()
                right_index += 1
            return adjust - 1
        index = 0
        max_adjust = 0
        s_len = len(s)
        for i in range(s_len):
            if i+1 < s_len:
                if s[i+1] == s[i]: # 中心为双数
                    adjust = find_left_right(s, i+0.5, 0.5)
                    if adjust > max_adjust:
                        index = i+0.5
                        max_adjust = adjust
                if s[i+1] == s[i-1]: # 中心为单数，索引-1为相同char
                    adjust = find_left_right(s, i, 0)
                    if adjust > max_adjust:
                        index = i
                        max_adjust = adjust
        return s[int(index - max_adjust): int(index +1 + max_adjust)]


# 提交答案中速度最快的一档
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            start = max(i - len(res) -1, 0)
            temp = s[start: i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res

a = Solution()
s = "cbbd"
# s = "cbbdadbb" # 强
print(a.longestPalindrome(s))