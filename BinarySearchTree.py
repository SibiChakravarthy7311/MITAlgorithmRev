class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self is None:
            return Node(data)
        while(True):
            if(data <= self.data):
                if(self.left is None):
                    self.left = Node(data)
                    break
                else:
                    self = self.left
            elif (data > self.data):
                if (self.right is None):
                    self.right = Node(data)
                    break
                else:
                    self = self.right

    def insertR(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node
                    
    def search(self, data):
        currentNode = self
        while currentNode is not None:
            if(data < currentNode.data):
                currentNode = currentNode.left
            elif (data > currentNode.data):
                currentNode = currentNode.right
            else:
                return currentNode
        return False

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node, end=" ")
        self.inOrder(node.right)

    def levelOrder(self):
        q = []
        q.append(self)
        while q:
            cur = q.pop(0)
            if(cur.left):
                q.append(cur.left)
            if (cur.right):
                q.append(cur.right)
            print(cur.data, end=' ')

    def inorder(self):
        node = self
        if node.left is not None:
            node.left.inorder()
        print(node.data, end=" ")
        if node.right is not None:
            node.right.inorder()

    def deleteNode(self, root, data):
        if not root:
            return None

        if root.data == data:
            if(not root.left and not root.right):
                return None
            elif(root.left and root.right):
                pnt = root.right
                while pnt.left:
                    pnt = pnt.left
                root.data = pnt.data
                root.right = self.deleteNode(root.right, root.data)
            elif(root.left):
                return root.left
            elif(root.right):
                return root.right
        elif root.data > data:
            root.left = self.deleteNode(root.left, data)
        elif root.data < data:
            root.right = self.deleteNode(root.right, data)
        return root

    def height(self, data):
        node = self.search(data)
        if(node):
            height = self.findHeight(node)
        else:
            return None
        return height

    def findHeight(self, node):
        if node is None:
            return -1
        return max(self.findHeight(node.left)+1, self.findHeight(node.right)+1)

    def __str__(self):
        return str(self.data)


t = Node(4)
# t.insertR(t, 2)
# t.insertR(t, 1)
# t.insertR(t, 3)
# t.insertR(t, 6)
# t.insertR(t, 5)
# t.insertR(t, 7)
t.insert(2)
t.insert(1)
t.insert(3)
t.insert(6)
t.insert(5)
t.insert(7)
t.insert(8)
# t.inOrder(t)
# print()
# t.levelOrder()
# print()
# t.inorder()
# t.deleteNode(t, 7)
# print()
# t.inorder()
t.inorder()
print()
# print(t.height(9))
