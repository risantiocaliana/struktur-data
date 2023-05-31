class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        def PrintTree(self):
            if self.left:
                self.left.PrintTree()
                print( self.data),
                if self.right:
                    self.right.PrintTree()
                    def PreorderTraversal(self, root):
                        res = []
                        if root:
                            res.append(root.data)
                            res = res + self.PreorderTraversal(root.left)
                            res = res + self.PreorderTraversal(root.right)
                            return res
root = Node(2)#root
root.left = Node(3) #child kiri dari root
root.right = Node(5) #child kanan dari root
root.left.left = Node(7) #child kiri dari 3
root.left.right = Node(9) #child kanan dari 3
root.right.left = Node(11) #child kiri dari 5
root.right.right = Node(13) #child kanan dari 5