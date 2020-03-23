#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@Author     : Zoe
@File       : tree_lowestCommonAncestor.py 
@Time       : 2019-12-04 17:39
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        flag, common = self.contain_pq(root, p, q)
        return common

    def contain_pq(self, root, p, q):
        flag = p==root or q==root
        if root.left:
            left_flag, left_common = self.contain_pq(root.left, p, q)
            if left_common:
                return True, left_common
        else:
            left_flag, left_common = False, None
        if root.right:
            right_flag, right_common = self.contain_pq(root.right, p, q)
            if right_common:
                return True, right_common
        else:
            right_flag, right_common = False, None

        if flag+left_flag+right_flag==2:
            return True, root
        elif flag+left_flag+right_flag==1:
            return True, None
        else:
            return False, None


class Solution2:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans


class Solution3:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        def contain_pq(root, p, q):
            if not root:
                return False

            flag = p == root or q == root
            left_flag = contain_pq(root.left, p, q)
            right_flag = contain_pq(root.right, p, q)

            if flag + left_flag + right_flag == 2:
                self.ans = root

            return flag or left_flag or right_flag

        contain_pq(root, p, q)
        return self.ans


root = TreeNode(5)
left = TreeNode(4)
right = TreeNode(4)
root.left = left
root.right = right
c = Solution3()
print(c.lowestCommonAncestor(root, root, left).val)
