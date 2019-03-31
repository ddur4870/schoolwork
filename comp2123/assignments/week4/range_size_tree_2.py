import node
import tree_interface

class RangeSizeTree(tree_interface.RSTreeInterface):
    """
    Range Size Tree

    Implements the Range Size Tree interface.
    Supports insertion, removal and getting the node.
    """

    def __init__(self):
        """
        Initialise the tree, root node is none.
        """
        self.root = None

    def put(self, k):
        """
        Put the value K into the tree.

        Hint McHintFace: watch out for duplicates!
        :param k: The key to insert into the tree.
        """
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
        """
        Get the node(s) with key `k`.

        E.g.
              3
           /     \
          1       5
         / \     / \
        1   2   4   6


        get(1) => returns array of both 1 (parent 1), 1 (parent 3)
        NOTE: ordered LEFT TO RIGHT!

        :param k: The key to get.
        :return: Array of Node's with key K.
        """
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
        """
        Remove's the value from the tree.

        Note: with duplicates, find the "FIRST DEEPEST OCCURRENCE"

        E.g.
              3
           /     \
          1       5
         / \     / \
        1   2   4   6

        Remove (1)

              3
           /     \
          1       5
           \     / \
            2   4   6

        :param k: value to remove from the tree.
        :return: The removed Node. None if node not found OR cannot be removed.
        """
        pass

    def range_size(self, a, b):
        """
        Calculates the size between two keys.
        (Inclusive!)

        e.g.
          2
         / \
        1  3

        range_size(1, 1) => 1

        e.g. #2
                    5
                /       \
              3          7
            /   \      /   \
          2      4    6     8
         / \     \        /  \
        1   3     5      8   10

        range_size(3, 7) => 7

        :param a: A key to search between.
        :param b: A key to search between.
        :return: Number of nodes between the two keys.
        """
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
