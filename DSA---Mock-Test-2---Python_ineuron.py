#!/usr/bin/env python
# coding: utf-8

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator. 
# 
#  Example 1:
# Input: x = 4 Output: 2 Explanation: The square root of 4 is 2, so we return 2.
# Example 2:
# 
# Input: x = 8 Output: 2 Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
# Constraints:
# 
# 0 <= x <= 2^31 - 1

# In[4]:


def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x

    while True:
        mid = left + (right - left) // 2
        if mid > x / mid:
            right = mid - 1
        else:
            if (mid + 1) > x / (mid + 1):
                return mid
            left = mid + 1


# In[6]:


print(mySqrt(8))  


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# 
# Example 1:
# 
# Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 342 + 465 = 807.
# 
# Example 2:
# 
# Input: l1 = [0], l2 = [0] Output: [0]
# 
# Example 3:
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] Output: [8,9,9,9,0,0,0,1]
# 
#  
# 
# Constraints:
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9 It is guaranteed that the list represents a number that does not have leading zeros.

# In[8]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum_val = x + y + carry
        carry = sum_val // 10
        curr.next = ListNode(sum_val % 10)
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        curr.next = ListNode(carry)

    return dummy.next


# In[9]:


# Example 1
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
# Traverse the resulting linked list to get the output: [7, 0, 8]
while result:
    print(result.val, end=' ')
    result = result.next


# In[ ]:




