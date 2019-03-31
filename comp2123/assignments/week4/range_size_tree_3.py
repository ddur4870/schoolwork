import node
import tree_interface

class RangeSizeTree(tree_interface.RSTreeInterface):

	def __init__(self):
		self.root = None
	def put(self, k):
		new_node = node.Node(k)

		if(self.root==None):

			self.root=new_node
		else:
			current_node = this.root
			while(true):
				if (k<=current_node.get_key() and currentNode.get_left()==None):
					new_node.set_parent(current_node)
					currentNode.set_left(new_node)
					currentNode.increment_subtree()
					break

			elif(k>current_node.get_key() and current_node.get_right()==None):
					current_node.increment_subtree()
					current_node.set_right(new_node)
					new_node.set_parent(current_node)
					break

			elif(k<=current_node.get_key()):
					current_node.increment_subtree()
					current_node=current_node.get_left()

					continue

			elif (k > current_node.get_key()):

					current_node.increment_subtree()
					current_node=current_node.get_right()

					continue
			else:
				print("something went wrong")
				pass

	def get(self, k):
		node_list=[]
		current_node = self.root
		while(true):
			if (current_node==None):
				break
			else:
				if (k==current_node.get_key())
					node_list.append(current_node)
					current_node= current_node.get_left()
				else:
					if (k<current_node.get_key()):
						current_node=current_node.get_left()
					elif(k>current_node.get_key()):
						currentNode=currentNode.getRight()
		return node_list

	def remove(self, k):
        	pass

	def range_size(self, a, b):
        	pass

################################################################################
# The following functions are not tested
# They are provided for you to run and test.
################################################################################

def main():
    pass


if __name__ == "__main__":
    print("Running main method of RangeSizeTree")
    main()
