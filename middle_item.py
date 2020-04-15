"""
Find the middle item in a singly linked list, 
or two middle items if it contains an even 
number of nodes.
"""

#singly linked list = linked list that only iterates in one direction
#list with odd length items = []
#list with even length items = []
#

# Definition for singly-linked list.

odd_list = [1,2,3,4,5,6,7]
even_list = [1,2,3,4,5,6,7,8]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        new_list = []
        
        while node != None:
            new_list.append(node)
            node = node.next
        length = len(new_list)
        middle_index = length // 2  
            
        middle_node = new_list[middle_index]
        return middle_node