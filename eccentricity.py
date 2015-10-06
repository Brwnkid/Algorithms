# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 21:47:38 2014

@author: nicholasclark
"""

import operator
def eccentricity(Graph):
    citylist = []
    for city in Graph.keys():
        citylist.append(city)
    e_list = {}
    for root in citylist:
        dist = {}
        dist2 = {}
        parent = {}
        inTree = {}
        for city in citylist:
            dist[city] = float('inf')
            inTree[city] = False
            dist2[city] = float('inf')
        dist[root] = 0
        inTree[root] = True
        parent[root] = 0
        n = len(citylist)
        for stage in range(0,n):
        #find city "u" with the minimum distance value... ugly I know
            u = reduce(lambda x,y: x if dist[x]<=dist[y] else y, dist.iterkeys())
            #save the network distance for each node
            dist2[u] = dist[u]
            inTree[u] = True
            for v in Graph[u]:  #all cities adjacent to city "u"
                if not inTree[v]:   #update distance/parent values
                    if dist[u] + s_distance(u,v) < dist[v]:
                        dist[v] = dist[u] + s_distance(u,v)
                        parent[v] = u
        #delete the key with the minimum distance so we can use min again
            del dist[u]
        maxdist = max(dist2.values())
        #save the max graph distance (eccentricity) for each city
        e_list[root] = maxdist
    #sort the eccentricity distances and print
    sorted_elist = sorted(e_list.items(), key=operator.itemgetter(1))
    for i in sorted_elist:
        print i