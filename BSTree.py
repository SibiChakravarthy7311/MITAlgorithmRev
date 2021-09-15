class BST:
    def __init__(self, value):
        self.value=value
        self.right=None
        self.left=None

    def insert(self, value):
        currentNode=self
        while currentNode is not None:
            if value<currentNode.value:
                if currentNode.left==None:
                    currentNode.left=BST(value)
                    break
                else:
                    currentNode=currentNode.left
