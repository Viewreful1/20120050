import sys
r = lambda: sys.stdin.readline().strip().split()

N, M, V = map(int, r())
def dfs(graph, start):
    stack = []
    seq = []
    visited = [False] * (N+1)
    cur = 0
    stack.append(start)
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        for i in reversed(graph[cur]):
            if not visited[i]:
                stack.append(i)
        visited[cur] = True
        seq.append(cur)
    return seq
    
def bfs(graph, start):
    queue = []
    seq = []
    visited = [False] * (N+1)
    
    cur = 0
    queue.append(start)
    while queue:
        cur = queue.pop(0)
        if visited[cur]:
            continue
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
        visited[cur] = True
        seq.append(cur)
    return seq
    
v = list(set() for _ in xrange(N+1))
for _ in xrange(M):
    f, t = map(int, r())
    v[f].add(t)
    v[t].add(f)

for i in xrange(1, N+1):
    v[i] = sorted(list(v[i]))
    
print ' '.join(map(str, dfs(v, V)))
print ' '.join(map(str, bfs(v, V)))