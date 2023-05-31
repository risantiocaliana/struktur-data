class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        print( self.data),
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

root = Node(6)#root
root.left = Node(4) #child kiri dari root
root.right = Node(12) #child kanan dari root
root.left.left = Node(3) #child kiri dari 3
root.left.right = Node(5) #child kanan dari 3
root.right.left = Node(10) #child kiri dari 5
root.right.right = Node(2) #child kanan dari 5
root.right.left.left = Node(8) #child kanan dari 5
root.right.left.right = Node(11) #child kanan dari 5
root.PrintTree()
