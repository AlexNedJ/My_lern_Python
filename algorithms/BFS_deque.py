#как можно самому реализовать очередь (queue) без deque и без встроенных библиотек
class Queue:
    def init(self):
        self.items = []

    def enqueue(self, item):   # Добавить в конец
        self.items.append(item)

    def dequeue(self):         # Удалить из начала
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

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
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right

    def bfs(self):
        if not self.root_node:
            return

        queue = Queue()
        queue.enqueue(self.root_node)

        while not queue.is_empty():
            node = queue.dequeue()
            print(node.value, end=' ')

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

tree = BinaryTree()
for val in [10, 5, 15, 2, 7, 20]:
    tree.insert(val)

tree.bfs()
# 👉 10 5 15 2 7 20