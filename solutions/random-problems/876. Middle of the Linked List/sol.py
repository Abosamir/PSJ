# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        current_node = head
        number_of_nodes = 1
        while current_node.next:
            number_of_nodes += 1
            current_node = current_node.next
        middle_node = number_of_nodes //2
        current_node = head
        i = 0
        while i != middle_node:
            current_node = current_node.next
            i += 1
        return current_node
        