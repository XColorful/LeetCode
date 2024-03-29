# 7. 整数反转

# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

# 假设环境不允许存储 64 位整数（有符号或无符号）。

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(x)[:0:-1]
            num = -int(s)
        else:
            s = str(x)[::-1]
            num = int(s)
        return num if -2**31 <= num < 2**31 else 0