# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

# 请你实现这个将字符串进行指定行数变换的函数：

# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        container = [ "" for _ in range(numRows) ]
        index = 0
        max_index = numRows - 1
        for char in s:
            container[index] += char
            if index == 0:
                turn = 1
            elif index == max_index:
                turn = -1
            index += turn
        return "".join(container)