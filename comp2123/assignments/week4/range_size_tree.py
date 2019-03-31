import node
import tree_interface

class RangeSizeTree(tree_interface.RSTreeInterface):
	def __init__(self):
		self.root = None
		self.current_node = None
		self.list_visited = []
	def current(self,k):
		self.current_node = k

	def get(self, k):
		print("the current node: "+ str(self.current_node)) ##
		if(self.current_node == None):
			print("there is no current nodes")
			return None
		self.list_visited.append(self.current_node)
		if(self.current_node.get_key() == k):
                #temp variable store and then reset the current node to top
			print("found it! The object is at " + str(self.current_node) + "with key: "+ str(self.current_node.get_key()))
			temp = self.current_node
			self.current(root)
			return temp
		elif(k<self.current_node.get_key()):
			next_left = self.current_node.get_left()
			self.current_node = next_left
			self.get(k)
		else:
			next_right = self.current_node.get_right()
			self.current_node = next_right
			self.get(k)

	def put(self, k):
		if(self.root==None or self.current_node == None):
			self.current(k)
			self.root = k
		result = get(k)
		if result == None: ##not in the tree yet
			if(len(self.list_visited)<1):
				print("fail list append didnt work")
			last_visited = self.list_visited[len(list_visited)-1]
			if(last_visited.get_key()>k.get_key()): ##assuming that k given is a node type already NOT an int then youd declare
				last_visited.set_left(k)
				k.set_parent(last_visited)
			else:
				last_visited.set_right(k)
				k.set_parent(last_visited)

		else:		##something with the key is already in the tree
			pass
			##remove whatever has the current key and then add the new one
			##remove(result)
			##self.put(k)
	def remove(self, k):

		result1=get(k)
		if result1 == None:
			print("that isnt in the tree")
			pass
		if result1.get_right()== None and result1.get_left()==None:
			del result1
		if result1.get_right() == None or result1.get_left()==None:
			child1 = True
			child2 = False
		else:
			child1=False
			child2=True
		if child1:
			##find whethe rhas a right or a left
			if result1.get_right()==None:
				ourchild=result1.get_left()
				ourparent=result1.get_parent()
				del result1
				ourchild.set_parent(ourparent)
				ourparent.set_left(ourchild)
			elif result1.get_left()==None:
				ourchild=result1.get_right()
				ourparent=result1.get_parent()
				del result1
				ourchild.set_parent(ourparent)
				ourparent.set_right(ourchild)
		if child2:
			null
		pass

	def range_size(self, a, b):
		pass

################################################################################
# The following functions are not tested
# They are provided for you to run and test.
################################################################################

def main():
	my_tree = RangeSizeTree()
	first_node = node.Node(3)
	second_node = node.Node(1)
	my_tree.put(first_node)
	my_tree.put(second_node)
	print("first nodes right: "+str(first_node.get_right()))
	print("first nodes left: "+ str(first_node.get_left()))
	if first_node.get_right() != None:
		print(str(first_node.get_right().get_key()))
	if first_node.get_left() != None:
		print(str(first_node.get_left().get_key()))
	print("attempt to find key 2")
	my_tree.get(2)
	print("attempt to find key 3")
	my_tree.get(3)

if __name__ == "__main__":
    print("Running main method of RangeSizeTree")
    main()

