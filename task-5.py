import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір у форматі HEX
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла


def build_binary_tree():
    """Створює приклад бінарного дерева для демонстрації."""
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)
    return root


def generate_color_gradient(n):
    """Генерує список кольорів RGB у відтінках синього від темного до світлого."""
    colors = []
    for i in range(n):
        intensity = int(255 * (i / (n - 1)))  # Збільшення яскравості
        hex_color = f'#{intensity:02X}{intensity:02X}FF'  # Відтінки синього
        colors.append(hex_color)
    return colors


def bfs_traversal(root):
    """Обхід дерева в ширину з використанням черги."""
    if not root:
        return []

    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


def dfs_traversal(root):
    """Обхід дерева в глибину з використанням стеку."""
    if not root:
        return []

    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)

        # Додаємо правий елемент першим, щоб лівий оброблявся першим
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додає вузли та ребра в граф для побудови дерева."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)


def draw_tree(tree_root, visited_nodes):
    """Візуалізує дерево та показує кожен крок обходу з унікальним кольором."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    # Присвоюємо кольори вузлам згідно з порядком обходу
    colors = generate_color_gradient(len(visited_nodes))
    for i, node in enumerate(visited_nodes):
        node.color = colors[i]

    # Готуємо граф для візуалізації
    node_colors = [node.color for node in visited_nodes]
    labels = {node.id: node.val for node in visited_nodes}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2000, node_color=node_colors)
    plt.show()


# Створюємо дерево
root = build_binary_tree()

# Виконуємо обхід у ширину (BFS) і візуалізуємо
bfs_nodes = bfs_traversal(root)
print("Обхід в ширину (BFS):", [node.val for node in bfs_nodes])
draw_tree(root, bfs_nodes)

# Виконуємо обхід у глибину (DFS) і візуалізуємо
dfs_nodes = dfs_traversal(root)
print("Обхід в глибину (DFS):", [node.val for node in dfs_nodes])
draw_tree(root, dfs_nodes)
