class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.rank = 1

    def insert(self, data):
        node = self
        fl = False
        if node is None:
            return Node(data)
        while(True):
            if(data <= node.data):
                if(node.left is None):
                    if(abs(node.data-data) >= 3):
                        fl = True
                    break
                else:
                    node = node.left
            elif (data > node.data):
                if (node.right is None):
                    if (abs(node.data - data) >= 3):
                        fl = True
                    break
                else:
                    node = node.right
        node = self
        if(fl):
            while (True):
                if (data <= node.data):
                    node.rank += 1
                    if (node.left is None):
                        node.left = Node(data)
                        break
                    else:
                        node = node.left
                elif (data > node.data):
                    node.rank += 1
                    if (node.right is None):
                        node.right = Node(data)
                        break
                    else:
                        node = node.right

    def inorder(self):
        node = self
        if node.left:
            node.left.inorder()
        print(node)
        if node.right:
            node.right.inorder()
            
    def planeCount(self, data):
        count = 0
        node = self
        while(True):
            if(not node):
                return count
            if(node.data == data):
                if(node.left):
                    count += node.left.rank
                    # print("Node.left.data:", node.left.data, "Node.left.rank", node.left.rank)
                break
            elif(node.data > data):
                node = node.left
            elif (node.data < data):
                # print("Node.data:", node.data, "Data:", data)
                count += 1
                if (node.left):
                    count += node.left.rank
                    # print("Node.left.data:", node.left.data, "Node.left.rank", node.left.rank)
                node = node.right
        return count

    def __str__(self):
        return "Node.data:"+str(self.data)+"\tNode.rank:"+str(self.rank)


t = Node(49)
t.insert(46)
t.insert(79)
t.insert(64)
t.insert(83)
t.insert(43)
t.inorder()
print()
print(t.planeCount(83))
