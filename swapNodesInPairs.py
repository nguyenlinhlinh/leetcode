# https://leetcode.com/problems/swap-nodes-in-pairs/




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        first = None
        second = None
        third = head
        counter = 1
        currentHead = head
        while third:
            if counter % 2 == 0:
                fourth = third.next
                # Swap
                second, third = third, second
                second.next = third
                third.next = fourth

                if first:
                    first.next = second
                else:
                    currentHead = second
                    
            first = second
            second = third
            third = third.next
            counter += 1                    
        return currentHead
    

# Test cases
head = ListNode(1)
current = head
for i in range(2, 5):
    current.next = ListNode(i)
    current = current.next

s = Solution()
head = s.swapPairs(head)
node = head
while node:
    print(node.val)
    node = node.next
