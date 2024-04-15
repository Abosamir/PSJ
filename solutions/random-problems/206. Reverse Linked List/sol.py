# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(self, head):

    prev_node = None
    current_node = head

    while current_node:

        # make the process of reverse
        next_node = current_node.next
        current_node.next = prev_node

        # Update each node with its new node
        prev_node = current_node
        current_node = next_node
    
    return prev_node