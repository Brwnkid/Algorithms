# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 16:33:57 2014

@author: nicholasclark
"""
import operator
def dilation(Graph, root):
    dist = {}
    parent = {}
    inTree = {}
    dilationDist = {}
    citylist = []
    for city in Graph.keys():
        citylist.append(city)
    for city in citylist:
        dist[city] = float('inf')
        inTree[city] = False
        dilationDist[city] = float(0)
    dist[root] = 0
    inTree[root] = True
    parent[root] = 0
    n = len(citylist)
    for stage in range(0,n):
        #find city "u" with the minimum distance value... ugly I know
        u = reduce(lambda x,y: x if dist[x]<=dist[y] else y, dist.iterkeys())
        #save dilation distance and avoid dividing by zero
        if u != root:        
            dilationDist[u] = dist[u]/s_distance(root,u)
        inTree[u] = True
        for v in Graph[u]:  #all cities adjacent to city "u"
            if not inTree[v]:   #update distance/parent values
                if dist[u] + s_distance(u,v) < dist[v]:
                    dist[v] = dist[u] + s_distance(u,v)
                    parent[v] = u
        #delete the key with the minimum distance so we can use min again
        del dist[u]
#    sort and print
    sorted_dil = sorted(dilationDist.items(), key=operator.itemgetter(1))
    for i in sorted_dil:
        print i