#Creating Graph
visited = set()
n,e = map(int,input().split())
graph = {}
for i in range(1,n+1):
    graph[i] = []

for _ in range(e):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

 
def dfs(node,lst):
    visited.add(node)
    lst.append(node)
    for child in graph[node]:
        if child not in visited:
            dfs(child,lst)

ans = []
for i in range(1,n+1):
    if i not in visited:
        lst = []
        dfs(i,lst)
        ans.append(lst)
print(ans)


