def clustering(Graph):
  sets = {}
  edges = {}
  InTree = []
  for v in Graph:
      sets[v]= set([v]);
      for u in Graph[v]:
          if (u,v) not in edges.keys() and (v,u) not in edges.keys():
              edges[(u,v)] = s_distance(v,u)
  sorted_edges = sorted(edges.items(), key=operator.itemgetter(1))
  print sorted_edges
  for edge in sorted_edges:
      if sets[edge[0][0]] != sets[edge[0][1]]:
          InTree.append(edge)
          sets[edge[0][0]] = sets[edge[0][0]].union(sets[edge[0][1]])
          sets[edge[0][1]] = sets[edge[0][0]]
          for i in sets:
              if edge[0][0] in sets[i] or edge[0][1] in sets[i]:
                  sets[i] = sets[edge[0][0]]
  for i in range(0,9):
    InTree.pop()
  connected = {}
  for edge in InTree:
    connected[edge[0][0]] = set([edge[0][0]])
    connected[edge[0][1]] = set([edge[0][1]])
  for edge in InTree:
    connected[edge[0][0]] = connected[edge[0][0]].union(connected[edge[0][1]])
    connected[edge[0][1]] = connected[edge[0][0]]
    for i in connected:
      if edge[0][0] in connected[i] or edge[0][1] in connected[i]:
          connected[i] = connected[edge[0][0]]
  toprint = {}
  for i in connected:
    #print connected[i]
    my_list = list(connected[i])
    if my_list[1] not in toprint.keys():
      print connected[i]
      toprint[my_list[1]] = ()
  citylist = []
  for city in Graph.keys():
    citylist.append(city)
  for i in citylist:
    if i not in connected.keys():
      print i
