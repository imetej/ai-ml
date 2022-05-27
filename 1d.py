from queue import PriorityQueue

vertices = 10
graph = [[] for i in range(vertices)]

def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def best_first_search(source, target, vertices):
    visited = [0] * vertices
    visited[source] = True
    pq = PriorityQueue()
    pq.put((0, source))
    print("Path : ", end="")
    while not pq.empty():
        u = pq.get()[1]
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))
    print()

add_edge(0, 1, 12)
add_edge(0, 2, 4)
add_edge(1, 3, 7)
add_edge(1, 4, 3)
add_edge(2, 5, 8)
add_edge(2, 6, 2)
add_edge(5, 7, 4)
add_edge(6, 8, 9)
add_edge(6, 9, 1)

source = 0
target = 9
best_first_search(source, target, vertices)