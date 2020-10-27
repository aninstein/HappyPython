#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目：重建二叉树
题目链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

知识点：

    前序遍历列表：第一个元素永远是 【根节点 (root)】
    中序遍历列表：根节点 (root)【左边】的所有元素都在根节点的【左分支】，【右边】的所有元素都在根节点的【右分支】

算法思路：

    通过【前序遍历列表】确定【根节点 (root)】
    将【中序遍历列表】的节点分割成【左分支节点】和【右分支节点】
    递归寻找【左分支节点】中的【根节点 (left child)】和 【右分支节点】中的【根节点 (right child)】

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        # 获取根节点
        root = preorder[0]
        rootNode = TreeNode(root)
        preorder.remove(root)

        # 子树
        left_tree = None
        temp_tree = list()
        is_tree = False
        for item in inorder:
            temp_tree.append(item)
            if root == item:
                is_tree = True
                temp_tree.remove(item)
                left_tree = temp_tree
                temp_tree = list()

        if not is_tree:
            return None

        right_tree = temp_tree
        Solution().buildTree(preorder, left_tree)
        Solution().buildTree(preorder, right_tree)
        return rootNode
