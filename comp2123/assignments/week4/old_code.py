    def put(self, k):
        """
        Put the value K into the tree.

        Hint McHintFace: watch out for duplicates!
        :param k: The key to insert into the tree.
        """
		if self.root == None
			self.list.append(k)
			new_node = Node.node(k)
			self.root = new_node
			self.node_list.append(new_node)
			self.key_list.append(new_node)
		else{
			new_node = Node.node(k)
			current_node = self.root
			if(current_node.get_key() == k):
				current_node.set_left(new_node)
				new_node.set_parent(current_node)
				self.root=node_list[0]
