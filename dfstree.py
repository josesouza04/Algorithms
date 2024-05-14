'''
    Adapted DFS algorithm to traverse a binary tree
    It returns the sum of the root-to-leaf paths

    Taken by: https://www.youtube.com/watch?v=v8eChm8rkx4
'''

class TreeNode: 
    def __init__(self, key : int = 0, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)
    
    def isLeaf(self):
        return self.left == None and self.right == None
    
def sumNumbers(root: TreeNode) -> int:
    total = ''
    def dfs(root, total):
        if root:
            if root.isLeaf():
                return int(total + str(root.key))
        
        total += str(root.key)
        return dfs(root.left, total) + dfs(root.right, total)
    return dfs(root, total)

def main():
    # Create a binary tree
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(sumNumbers(root)) # return 25
    return 0

if __name__ == '__main__':
    main()
