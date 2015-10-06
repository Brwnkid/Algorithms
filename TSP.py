def TSP(Graph):
  sets = {}
  edges = {}
  InTree = []
  cities = set()
  for v in Graph:
    cities.add(v)
    sets[v]= set([v]);
    for u in Graph[v]:
          if (u,v) not in edges.keys() and (v,u) not in edges.keys():
              edges[(u,v)] = s_distance(v,u)
  sorted_edges = sorted(edges.items(), key=operator.itemgetter(1))
  for edge in sorted_edges:
      if sets[edge[0][0]] != sets[edge[0][1]]:
          InTree.append(edge)
          sets[edge[0][0]] = sets[edge[0][0]].union(sets[edge[0][1]])
          sets[edge[0][1]] = sets[edge[0][0]]
          for i in sets:
              if edge[0][0] in sets[i] or edge[0][1] in sets[i]:
                  sets[i] = sets[edge[0][0]]
  MST_sum = 0
  for i in InTree:
    MST_sum = MST_sum + i[1]
  print "MST total distance", MST_sum, "miles"
  
  doubleTree = []
  #doubled edges for MST
  for edge in InTree:
    doubleTree.append(edge)
  #add edges second time separately to make sure it goes through the edges at least once before going back.
  for edge in InTree:
    doubleTree.append(((edge[0][1],edge[0][0]),edge[1]))
  last_visited = doubleTree[0][0][0]
  visited = [last_visited]
  visited_cities = set()
  visited_cities.add(last_visited)
  while visited_cities != cities:
    for edge in doubleTree:
      if edge[0][0] == last_visited:
        visited.append(edge[0][1])
        last_visited = edge[0][1]
        visited_cities.add(last_visited)
        doubleTree.remove(edge)
        break
      elif edge[0][1] == last_visited:
        visited.append(edge[0][0])
        last_visited = edge[0][0]
        visited_cities.add(last_visited)
        doubleTree.remove(edge)
        break
  order_visited = []
  for i in visited:
    if i not in order_visited:
      order_visited.append(i)

  tour_sum = 0
  for i in range(len(order_visited)-1):
    tour_sum = tour_sum + s_distance(order_visited[i],order_visited[i+1])
  
  print "Order of cities visited:", order_visited
  print "Total miles traveled on tour", tour_sum, "miles"
  if tour_sum < 2*MST_sum:
    print "The length of the tour is less than 2*OPT[MST]"
  
TSP(G)
