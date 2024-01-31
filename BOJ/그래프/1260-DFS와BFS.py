from collections import deque
n, m, v = map(int, input().split())
graph = [[]*m for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

def bfs():
    queue = deque()
    visited = []
    queue.append(v)
    visited.append(v)
    while queue:
        vertex = queue.popleft()
        for node in graph[vertex]:
            if node not in visited:
                queue.append(node)
                visited.append(node)
    return visited

visited_node = []
def dfs(node, visited_node):
    visited_node.append(node)
    for nd in graph[node]:
        if nd not in visited_node:
            dfs(nd, visited_node)
    return visited_node


b = bfs()
d = dfs(v, visited_node)

print(*d)
print(*b)