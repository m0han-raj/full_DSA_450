# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        while head!=None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        curr = head
        mx = curr.val

        while curr and curr.next:
            if curr.next.val < mx:
                curr.next = curr.next.next
            else:
                curr = curr.next
                mx = curr.val
        return self.reverse(head)

        curr = head
        mx = curr.val

        while curr and curr.next:
            if curr.next.val < mx:
                curr.next = curr.next.next
            else:
                curr = curr.next
                mx = curr.val
        return self.reverse(head)