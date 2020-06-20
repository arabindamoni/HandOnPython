class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
        
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

###           10
###        5     15
###      3   6 11  20
###         
# 


def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 

def preorder(root): 
    if root: 
        print(root.val)
        inorder(root.left)         
        inorder(root.right) 

def postorder(root): 
    if root: 
        inorder(root.left)
        inorder(root.right) 
        print(root.val)    

# return sum of all node values
 
def sum_(root):
    if not root: return 0
    l = inorder(root.left)
    r = inorder(root.right)
    return l + r + root.val 

def sum_diff(root):
    diff = 0
    diff = sum_(root.right) - sum_(root.left)
    return diff


# return height of tree 
# height(root) = 1 + max(height(root.left), height(root.right)
def height(root):
    if root == None:
        return 0
    l = height(root.left)
    r = height(root.right)
    if r > l:
        return r+1
    else:
        return l+1
    return 

###           10
###        5     15
###      3   6 11  20
###    search(root, val) = search(root.left, val) or search(root.right, val) or val == root.val
#   
# return true if val exists in tree
def search(root, val):
    if root == None:
        return False
    # return search(root.left, val) or search(root.right, val) or val == root.val
    if root.val == val:
        return True
    elif root.val > val:
        return search(root.left, val)
    else:
        return search(root.right, val)



r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

# sum_diff(root.left) --> 5 node

# print("Inorder")
# inorder(r)
# print("Preorder")
# preorder(r)
# print("Postorder")
# print(height(r))