class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def insert(self, node, data):
        if not node:
            return Node(data)
        if data <= node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
            
        node.height = max(self.getHeight(node.left)+1, self.getHeight(node.right)+1)

        # print("node.left.height:", self.getHeight(node.left))
        # print("node.right.height:", self.getHeight(node.right))
        balance = self.getBalance(node)
        # print("Node:", node.data, " Balance:", balance)

        if balance > 1 and data > node.left.data:
            # print("Double Right Rotate")
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        elif balance > 1 and data < node.left.data:
            # print("Right Rotate")
            return self.rightRotate(node)
        elif balance < -1 and data < node.right.data:
            # print("Double Left Rotate")
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        elif balance < -1 and data > node.right.data:
            # print("Left Rotate")
            return self.leftRotate(node)

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
        return None

    def heightOf(self, data):
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
    
    def getHeight(self, node):
        if not node:
            return -1
        return node.height
    
    def getBalance(self, node):
        if not node:
            return -1
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def leftRotate(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node

        node.height = max(self.getHeight(node.left) + 1, self.getHeight(node.right) + 1)
        temp.height = max(self.getHeight(temp.left)+1, self.getHeight(temp.right)+1)

        return temp

    def rightRotate(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node

        node.height = max(self.getHeight(node.left) + 1, self.getHeight(node.right) + 1)
        temp.height = max(self.getHeight(temp.left) + 1, self.getHeight(temp.right) + 1)
        return temp
    
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(node.data, end="  ")
        self.inorder(node.right)

    def levelOrder(self):
        q = []
        q.append(self)
        while q:
            cur = q.pop(0)
            if(cur.left):
                q.append(cur.left)
            if (cur.right):
                q.append(cur.right)
            print(cur.data, end='  ')

    def __str__(self):
        return str(self.data)+" "


# a = Node(4)
# a.insert(a, 2)
# a.insert(a, 1)
# a.insert(a, 3)
# a.insert(a, 6)
# a.insert(a, 5)
# a.insert(a, 7)
# a.insert(a, 8)

# a = Node(1)
# a = a.insert(a, 2)
# a = a.insert(a, 4)

# a = Node(1)
# a.right = Node(2)
# a.right.right = Node(4)
# a = a.leftRotate(a)

a = Node(1)
a = a.insert(a, 2)
a = a.insert(a, 3)
a = a.insert(a, 4)
a = a.insert(a, 5)
a = a.insert(a, 6)
a = a.insert(a, 7)
a = a.insert(a, 8)

a.inorder(a)
print()
a.levelOrder()
print()
# print(a.heightOf(3))
