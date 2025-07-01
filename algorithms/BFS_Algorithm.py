from collections import deque  # очередь для BFS

class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def init(self):
        self.root_node = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root_node:
            self.root_node = new_node
            return

        current = self.root_node
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def bfs(self):
        if not self.root_node:
            return

        queue = deque()
        queue.append(self.root_node)

        while queue:
            node = queue.popleft()
            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(20)

tree.bfs()