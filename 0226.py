def invertTree(root):
    if not root: return
    
    root.left,root.right=root.right,root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return invertTree(root)
 
