# import graph

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}



def dfs(graph, start):
    visted = set()
    vertex = [start]

    while vertex:
        current = vertex.pop()

        if current not in visted:
            visted.add(current)
            vertex.extend(graph[current] - visted)

    return visted


def dfs_recursive(graph, start, visited):
    if visited is None:
        visited = set()

    visited.add(start)
    for vertex in graph[start] - visited:
        dfs_recursive(graph, vertex, visited)

    return visited



# def dfs_paths(graph, start, goal):
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         for nxt in graph[vertex] - set(path):
#             if nxt == goal:
#                 yield path + [nxt]
#             else:
#                 stack.append((nxt, path + [nxt]))











def dfs_paths(graph, start, end):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        for current in graph[vertex] - visited:
            if current == end:
                yield visited.add(curent)

            stack.extend(graph)




if __name__ == '__main__':
    a = dfs(graph, 'A')
    print(a)

    b = dfs_recursive(graph, 'A', None)

    print(b)

    print(list(dfs_paths(graph, 'A', 'F')))
