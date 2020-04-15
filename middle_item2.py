"""
This solution uses a time complexity of O(n) due to search time, and a space complexity of O(1) 
"""



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