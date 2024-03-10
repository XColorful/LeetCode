# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

# 算法的时间复杂度应该为 O(log (m+n)) 。

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 这个纯属扯淡，没算法
        combine = nums1 + nums2
        combine.sort()
        length = len(combine) / 2
        int_len = int(length)
        if length != int_len: return combine[int_len]
        else:
            length = int_len
            return (combine[int_len - 1] + combine[int_len]) / 2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = ( len(nums1) + len(nums2) + 1 ) // 2
        k2 = ( len(nums1) + len(nums2) + 2 ) // 2
        def helper(nums1,nums2,k): #本质上是找第k小的数
            if(len(nums1) <len(nums2) ):
                nums1, nums2 = nums2 , nums1 #保持nums1比较长
            if(len(nums2)==0):
                return nums1[k-1] # 短数组空，直接返回
            if(k==1):
                return min(nums1[0],nums2[0])  #找最小数，比较数组首位
            t = min(k//2,len(nums2)) # 保证不上溢
            if( nums1[t-1]>=nums2[t-1] ):
                return helper(nums1 , nums2[t:],k-t)
            else:
                return helper(nums1[t:],nums2,k-t)
        return ( helper(nums1,nums2,k1) + helper(nums1,nums2,k2) ) /2

# 作者：雅托不过不改名的惊鸿
# 链接：https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/277873/cong-yi-ban-dao-te-shu-de-fang-fa-dai-ma-jing-jian/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。