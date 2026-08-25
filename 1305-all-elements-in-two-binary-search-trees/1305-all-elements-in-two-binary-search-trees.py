# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder( root: Optional[TreeNode], elements: List[int]) -> None:
            if not root:
                return None
            inorder(root.left,elements)
            elements.append(root.val)
            inorder(root.right,elements)

            return root

        first_tree_elements=[]
        second_tree_elements=[]
        inorder(root1 , first_tree_elements)
        inorder(root2 , second_tree_elements)

        len1 = len(first_tree_elements)
        len2 = len(second_tree_elements)

        pointer1 = 0
        pointer2 = 0
        merged = []


        while pointer1 < len1 and pointer2 < len2:
            if first_tree_elements[pointer1] <= second_tree_elements[pointer2]:
                merged.append(first_tree_elements[pointer1])
                pointer1 +=1
            else:
                merged.append(second_tree_elements[pointer2])
                pointer2 +=1

        while pointer1 < len1:
            merged.append(first_tree_elements[pointer1])
            pointer1 += 1
        
        while pointer2 < len2:
            merged.append(second_tree_elements[pointer2])
            pointer2 += 1
        
        return merged