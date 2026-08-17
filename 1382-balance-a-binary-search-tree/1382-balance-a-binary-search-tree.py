# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []

        def inorder(node):
            if not node:
                return None

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

            return root
        inorder(root)

        def build(left,right):
            if left>right:
                return None
            mid = (left+right)//2

            root = TreeNode(nums[mid])

            root.left = build(left,mid-1)
            root.right = build(mid+1,right)

            return root
        
        return build(0,len(nums)-1)



