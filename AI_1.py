from collections import deque
def DFS ( adjacent, source , visited ,key ):
    if (source==key):
        return True
    visited[source]=True

    for node in adjacent[source]:
        if not visited[node]:
            if DFS(adjacent,node,visited,key):
                return True
    return False


def BFS(graph,q,visited,key):
    if not q

adjacent={
    0:[1,2],
    1:[0,3,4],
    2:[0,5],
    3:[1,6],
    4:[1],
    5:[2,7],
    6:[3],
    7:[5]
}

visit = [False] * len(adjacent) 
src = 0
k = 6

found=DFS(adjacent,src,visit,k)
print("Key Found:",found)