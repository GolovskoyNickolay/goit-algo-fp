import uuid
import networkx as nx
import matplotlib.pyplot as plt
import math


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла


def build_heap_tree(array):
    """Функція для побудови бінарного дерева із масиву (бінарна купа)."""
    if not array:
        return None

    nodes = [Node(key) for key in array]  # Створення вузлів із значень масиву

    # З'єднання вузлів відповідно до структури бінарної купи
    for i in range(len(array) // 2):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(array):
            nodes[i].left = nodes[left_index]
        if right_index < len(array):
            nodes[i].right = nodes[right_index]

    return nodes[0]  # Повертаємо корінь дерева


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


def draw_tree(tree_root):
    """Візуалізує дерево за допомогою NetworkX."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2000, node_color=colors)
    plt.show()


# Приклад масиву для бінарної купи
heap_array = [10, 15, 30, 40, 50, 100, 40]

# Побудова та візуалізація бінарної купи
heap_tree = build_heap_tree(heap_array)
draw_tree(heap_tree)