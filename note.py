if delete(self , data):
	if data > self.key:
		if self.lchild:
			self.lchild = self.lchild.delete(data)
			
	elif data < self.key:
		if self.rchild :
		self.rchild = self.rchild.delete(data)
		
	else:
		if self.lchild is None:
			temp = self.rchild 
			self = None
			return temp
			
		if self.rchild is None:
			temp = self.lchild
			self = None
			return temp
			
		node = self.rchild
		while node.lchild:
			node = self.lchild
		node.key = self.key
		self.rchild = self.rchild.delete(node.key)
	return self	
	
	

def insert(self , data):
	if self.key is None :
		return 
		
	if self.key == data:
		return
		
	if data < self.key	
		if self.lchild:
			self.lchild.insert(data)
		else:
		 self.lchild = BST(Data)
	else:
		if self.rchild:
			self.rchild.insert(data)
		else:
			self.rchild = BST(data)
			
def inorder(self):
	if self.lchild:
		self.lchild.inorder()
	
	print(self.data , end=" ")
	
	if self.rchild:
		self.rchild.inorder()


def preorder(self):
	print(self.data , end=" ")
	
	if self.lchild:
		self.lchild.preoreder()
	
	if self.rchild:
		self.rchild.preorder()
		
def postorder(self):
	if self.lchild:
		self.lchild.postorder()
		
	if self.rchild:
		self.lchild.postorder()
		
	print(self.data , end=" ")
	
	
	
def search(self , data):
	if self.key == data:
		return
		
	if data < self.key :
		if self.lchild:
			self.lchild.search(data)
		else:
			print("Node is not present")
			
			
	else:
		if self.rchild:
			self.rchild.search(data)
		else:
			print("Node is not present")
	
	
	

#AVL Tree 

class Node:
	def __init__(self , key):
		self.key = key 
		self.right = None
		self.left = None
		self.height = 1
		
def get_height(node):
    if not node:
        return 0 
    return node.height

		
def get_balance(node):
	if not node:
		return 0
    return get_height(node.left) - get_height(node.right)
		
	
def right_rotate(y):
	x = y.left 
	t2 = x.right
		
	x.right = y
	y.left = t2
	
	
	x.height = 1 + max(get_height(x.left) , get_height(x.right))
	y.height = 1 + max(get_height(y.left) , get_height(y.right))
	
    return x
  
def inorder(root):
    inorder(root.left)
    print(root.key , end=" ")
    inorder(root.right)
    
 
  
  
  
class Node :
    def __init__(self , key):
        self.key = key 
        self.right = None
        self.left = None 
        self.height = 1
        
def get_height(node):
    if not node :
        return 0
    return height
    
def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - (node.right)
    
def right_rotate(y):
    x = y.left
    t2 = x.right 
    
    y = x.right 
    t2 = y.left
    
    x.height = 1 + max(get_height(x.left) , get_height(x.right))
    y.height = 1 + max(get_height(y.left) , get_height(y.left))
    
    return x
    
    
def left_rotate(x):
    y = x.right
    t2 = y.left 
    
    y.left = x
    x.right = t2
    
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left) , get_height(y.right))
    
    return y
    
def left_left_rotate(z):
    y = z.left
    t3 = y.right
    
    y.right = z
    z.left = t3
    
    z.height = 1 + max(get_height(z.left) , get_height(z.right))
    y.height = 1 + max(get_height(y.left) , get_height(y.right))
    
    return z
    
    
    
       