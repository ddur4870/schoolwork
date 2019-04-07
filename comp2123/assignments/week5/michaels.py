
A = [[2, 2],[4,1],[5,4],[6,3]]


class Node:
    """
    Simple node in the binary tree.
    """

    def __init__(self, pv):

        self.left = None
        self.right = None
        self.parent = None
        self.p = pv[0]
        self.v = pv[1]

    def __repr__(self):
        p = str(self.p)
        v = str(self.v)
        return "(" + p + ", " + v + ") "

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, pv):
        new_node = Node(pv)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root

            while True:
                parent = current
                if (pv[1] < current.v):
                    current = current.left
                    if current is None:
                        parent.left = new_node
                        return
                else:
                    current = current.right
                    if current is None:
                        parent.right = new_node
                        return

    def construct(self,A):
        for pv in A:
            self.insert(pv)

    def printTree(self, head):
        if (head == None):
            return
        print(head.p, head.v)
        self.printTree(head.left)
        self.printTree(head.right)


r = Tree()
r.construct(A)
r.printTree(r.root)
print(r.root.right.left)
