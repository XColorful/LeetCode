# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_1 = False # 进位检查
        use_node = return_node = ListNode()
        n1, n2 = l1, l2
        while n1 or n2:
            sum = 0 # 单次加法的和
            try:
                sum += n1.val # 加上这一位
                n1 = n1.next # 换成下一位
            except: pass
            try:
                sum += n2.val
                n2 = n2.next
            except: pass

            if add_1: # 如果有遗留的进位
                sum += 1 # 加1
            use_node.next = ListNode(sum % 10) # 添加到返回列表的为一位数
            use_node = use_node.next

            if sum > 9: add_1 = True # 下一次循环仍进位
            else: add_1 = False # 下一次循环无进位

        # while循环结束
        if add_1 == True: use_node.next = ListNode(1) # 把漏掉的进位补上
        return return_node.next