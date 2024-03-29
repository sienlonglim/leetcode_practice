'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = set()
        def _max(root, n):
            if root.left:
                _max(root.left, n+1)
            if root.right:
                _max(root.right, n+1)
            if not root.left and not root.right:
                ans.add(n)

        if root:
            _max(root, 1)
            return max(ans)
        else:
            return 0
