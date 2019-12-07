file = open("input.txt")

orbit_graph = {}
for line in file:
    [key, value] = line.strip().split(")")
    orbit_graph.setdefault(key, []).append(value)
    orbit_graph.setdefault(value,[]).append(key)

visited = []
next = [('YOU', 0)]
count = -1
while next:
    (body, count) = next.pop(0)
    if body == 'SAN':
        print(count - 2)
        break
    visited.append(body)
    next += [(val, count+1) for val in orbit_graph[body] if val not in visited]
print(orbit_graph)