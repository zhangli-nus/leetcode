#coding: utf-8
import numpy as np


def dijkstra(G, v0, inf = np.inf):
    S, U = set(), set(G.keys())
    dis = dict((k, inf) for k in G.keys())
    dis[v0] = 0
    parent = dict((k, k) for k in G.keys())
    min_v = v0

    while U:
        S.add(min_v)
        U.remove(min_v)
        for k in G.keys():
            if k in G[min_v].keys():
                tmp = G[min_v][k] + dis[min_v]
                if tmp<dis[k]:
                    dis[k] = tmp
                    parent[k] = min_v
        min_d = np.inf
        for u in U:
            if dis[u]<min_d:
                min_d = dis[u]
                min_v = u
    return parent, dis


def kruskal(G):
    node = G.keys()
    parent = dict((k, k) for k in G.keys())
    all_edges = set()
    for key1 in G.keys():
        for key2 in G[key1].keys():
            all_edges.add((key1, key2))
    mst = set([node[0]])
    mst_edge = set()
    while len(mst)<len(node):
        print(len(mst), len(node))
        for edge in all_edges:
            v1, v2 = edge
            if v2<v1:
                v1, v2 = v2, v1
            if v1 in mst and v2 in mst:
                continue
            if (v1 in mst or v2 in mst) and parent[v1]!=parent[v2]:
                mst_edge.add(edge)
                mst.add(v1)
                mst.add(v2)
                parent[v2] = parent[v1]
                break
    return mst_edge, parent


if __name__ == '__main__':
    G = {
        'A': {'B': 10, 'C': 12, 'D': 20}
        ,'B': {'C': 20, 'A': 10, 'D': 30}
        ,'C': {'D': 5}
        ,'D': {}
    }
    v0 = 'A'
    parent, dis = dijkstra(G, v0)
    for k in G.keys():
        route = []
        v = k
        route.append(v)
        while parent[v]!=v0:
            v=parent[v]
            route.append(v)
        route.append(v0)
        print('k: ', k, 'dis: ', dis[k], 'route:', route)

    mst_edge, parent = kruskal(G)
    print(mst_edge, parent)
