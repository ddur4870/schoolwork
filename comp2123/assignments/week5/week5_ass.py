A=[[1,3],[3,2],[2,1]]

class Node:
	def __init__(self, pair):	##intializing the node class
		self.left=None		##intilising left child to None type
		self.right=None 	##initializing right child to None type
		self.parent=None 	##initilizing parent to none type
		self.p_val=pair[0] 	##defining the p value as the first in the pair
		self.v_val=pair[1] 	##defining the v value as the secons in the pair

class Tree:				##making the tree's class to help construct the tree
	def __init__(self):  		##initialising method to define the type
		self.root=None  	##setting the tree's root to nothing initially
	def add(self,A): 		##defines add function to the tree, takes array param
		given_list=A		##defines the given list as A
		given_list.sort() 	##gets list sorted by p_val for heap
		for pair in given_list:	##for each pair in the given list

			new_node=Node(pair)	##initialize a new node with the pair given
			if self.root ==None:	##if theres no defined root asign the new node to be the root
				self.root=new_node
			else:			##otherwise theres already a root and should define it as the current node
				current_node=self.root
				while(True):	##until broken iterate through the tree using the BST property
					parent_node = current_node
					if new_node.v_val < current_node.v_val: ##going through the tree using BST until finds empty space
						current_node=current_node.left
						if current_node == None: ##if the pair finds it's unoccupied space it will join and break
							parent_node.left=new_node
							break		##breaks the loop and algo is able to perform same for next pair
					else:
						current_node = current_node.right ##same as above but uses the RHS when v_val is larger
						if(current_node == None):
							parent_node.right=new_node
							break


	def print_tree(self,root):
		print("root: " + str(root.p_val) +","+str(root.v_val))
		print("roots left: " + str(root.left.p_val) + "," + str(root.left.v_val))
		print("root lefts right:" + str(root.left.right.p_val) + ","+str(root.left.right.v_val))

r=Tree()
r.add(A)
r.print_tree(r.root)



