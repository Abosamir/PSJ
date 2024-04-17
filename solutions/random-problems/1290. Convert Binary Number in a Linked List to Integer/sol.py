# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
            current_node = head

            list_of_values = []

            while current_node:
                list_of_values.append(current_node.val)
                current_node = current_node.next
            
            i = len(list_of_values)-1
            k = 0
            result = 0
            while i >= 0:
                result += 2**(k)*list_of_values[i]
                i -= 1
                k += 1
            
            return result
        