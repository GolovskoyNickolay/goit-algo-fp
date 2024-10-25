import heapq

class Graph:
    def __init__(self):
        self.edges = {}  # Зберігає список суміжних вершин для кожної вершини
        self.weights = {}  # Зберігає ваги ребер

    def add_edge(self, u, v, weight):
        # Додаємо ребро з вершини u в вершину v з вагою weight
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append(v)
        self.edges[v].append(u)  # Якщо граф неорієнтований
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight

def dijkstra(graph, start):
    # Ініціалізація
    min_heap = [(0, start)]  # Купа: (вага шляху, вершина)
    distances = {vertex: float('inf') for vertex in graph.edges}  # Відстані до вершин
    distances[start] = 0  # Відстань до стартової вершини дорівнює 0
    visited = set()  # Множина відвіданих вершин

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_vertex in visited:
            continue  # Якщо вершина вже відвідана, пропускаємо її

        visited.add(current_vertex)

        # Оновлення відстаней до суміжних вершин
        for neighbor in graph.edges[current_vertex]:
            weight = graph.weights[(current_vertex, neighbor)]
            distance = current_distance + weight

            # Якщо знайдено коротший шлях, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Приклад використання
if __name__ == "__main__":
    graph = Graph()
    # Додаємо ребра в граф (u, v, вага)
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 6)
    graph.add_edge('C', 'D', 3)

    # Запускаємо алгоритм Дейкстри з вершини 'A'
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    # Виводимо найкоротші шляхи
    print(f"Найкоротші шляхи від вершини '{start_vertex}':")
    for vertex, distance in shortest_paths.items():
        print(f"Відстань до вершини {vertex}: {distance}")
