class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_in_order(node):
    if not node:
        return
    dfs_in_order(node.left)        # Сначала левое поддерево
    print(node.value, end=' ')     # Потом текущий узел
    dfs_in_order(node.right)       # Потом правое поддерево

# Создаём дерево
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)
root.right.right.right =Node(3)
root.right.right.left = Node(8)

# Вывод: 2 5 7 10 15 20
dfs_in_order(root)

#DFS без рекурсии (на стеке)
def dfs_in_order_iterative(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.value, end=' ')
        current = current.right

dfs_in_order_iterative(root)