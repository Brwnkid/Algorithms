# We start with a function to parse each line of our dataset:

def parse_city(line):
  code, lat, long, name = line.split(None, 3)
  cityname, state = name.split(',')
  scode=code[1:-1]
  return scode, (float(long), float(lat))

# Our city data is embedded in function that maps the line parser to each line of data

UScityData = map(parse_city, """
[TCL] 33.23 87.62 Tuscaloosa,AL
[PHX] 33.43 112.02 Phoenix,AZ
[PGA] 36.93 111.45 Page,AZ
[TUS] 32.12 110.93 Tucson,AZ
[LIT] 35.22 92.38 Little Rock,AR
[SFO] 37.62 122.38 San Francisco,CA
[LAX] 33.93 118.40 Los Angeles,CA
[SAC] 38.52 121.50 Sacramento,CA
[SAN] 32.73 117.17 San Diego,CA
[SBP] 35.23 120.65 San Luis Obi,CA
[EKA] 41.33 124.28 Eureka,CA
[SJC] 37.37 121.92 San Jose,CA
[DEN] 39.75 104.87 Denver,CO
[DRO] 37.15 107.75 Durango,CO
[HVN] 41.27 72.88 New Haven,CT
[DOV] 39.13 75.47 Dover,DE
[DCA] 38.85 77.04 Washington/Natl,DC
[MIA] 25.82 80.28 Miami Intl,FL
[TPA] 27.97 82.53 Tampa Intl,FL
[JAX] 30.50 81.70 Jacksonville,FL
[TLH] 30.38 84.37 Tallahassee,FL
[ATL] 33.65 84.42 Atlanta,GA
[BOI] 43.57 116.22 Boise,ID
[CHI] 41.90 87.65 Chicago,IL
[IND] 39.73 86.27 Indianapolis,IN
[DSM] 41.53 93.65 Des Moines,IA
[ICT] 37.65 97.43 Wichita,KS
[LEX] 38.05 85.00 Lexington,KY
[NEW] 30.03 90.03 New Orleans,LA
[BOS] 42.37 71.03 Boston,MA
[PWM] 43.65 70.32 Portland,ME
[BGR] 44.80 68.82 Bangor,ME
[DET] 42.42 83.02 Detroit,MI
[STC] 45.55 94.07 St Cloud,MN
[MIN] 44.98 93.26 Minneapolis,MN
[DLH] 46.83 92.18 Duluth,MN
[STL] 38.75 90.37 St Louis,MO
[JAN] 32.32 90.08 Jackson,MS
[BIL] 45.80 108.53 Billings,MT
[BTM] 45.95 112.50 Butte,MT
[RDU] 35.87 78.78 Raleigh-Durh,NC
[INT] 36.13 80.23 Winston-Salem,NC
[OMA] 41.30 95.90 Omaha,NE
[LAS] 36.08 115.17 Las Vegas,NV
[EWR] 40.70 74.17 Newark,NJ
[ABQ] 35.05 106.60 Albuquerque,NM
[SAF] 35.62 106.08 Santa Fe,NM
[LRU] 32.30 106.77 Las Cruces,NM
[NYC] 40.77 73.98 New York,NY
[BUF] 42.93 78.73 Buffalo,NY
[ALB] 42.75 73.80 Albany,NY
[FAR] 46.90 96.80 Fargo,ND
[BIS] 46.77 100.75 Bismarck,ND
[CVG] 39.05 84.67 Cincinnati,OH
[COL] 39.98 82.98 Columbus, OH
[CLE] 41.42 81.87 Cleveland,OH
[OKC] 35.40 97.60 Oklahoma Cty,OK
[PDX] 45.60 122.60 Portland,OR
[MFR] 42.37 122.87 Medford,OR
[PIT] 40.35 79.93 Pittsburgh,PA
[PVD] 41.73 71.43 Providence,RI
[CHS] 32.90 80.03 Charleston,SC
[MEM] 35.05 90.00 Memphis,TN
[DAL] 32.90 97.03 Dallas,TX
[LBB] 33.65 101.82 Lubbock,TX
[IAH] 29.97 95.35 Houston,TX
[SAT] 29.53 98.47 San Antonio,TX
[ABI] 32.42 99.68 Abilene,TX
[ELP] 31.79 106.42 El Paso, TX
[SLC] 40.78 111.97 Salt Lake Ct,UT
[MPV] 44.20 72.57 Montpelier,VT
[RIC] 37.50 77.33 Richmond,VA
[SEA] 47.45 122.30 Seattle,WA
[ALW] 46.10 118.28 Walla Walla,WA
[GRB] 44.48 88.13 Green cityBay,WI
[MKE] 42.95 87.90 Milwaukee,WI
[CYS] 41.15 104.82 Cheyenne,WY
[SHR] 44.77 106.97 Sheridan,WY
[MAD] 43.07 89.400 Madison, WI
[FLG] 35.20 111.63 Flagstaff, AZ
[KAN] 39.09 94.57 Kansas City, MO
[LOU] 38.25 85.76 Louisville, KY
[PHI] 39.95 75.16 Philadelphia, PA
[NAS] 36.16 86.78 Nashville, TN
[KNO] 35.97 83.94 Knoxville, TN
[TAM] 27.97 82.46 Tampa, TN
[PRO] 41.82 71.42 Providence, RI
""".strip().splitlines())




# Our aim is to study functions that give us transit costs for each pair of cities.
# So we first turn to making the city to location function by using a hash table
# that has (key,value) pairs using citycodes for keys and citylocaton as values.


cityhash= { citycode : cityloc for (citycode,cityloc) in UScityData}
#print sorted(cityhash)
#print cityhash
print cityhash['CVG'] # (84.67, 39.05)
 

# We write a function that calculates the spherical (crow-fly) milage distance between
# pairs of cities using long,lat data

import math
def s_distance(loc1, loc2):
    (long1,lat1)= cityhash[loc1]
    (long2,lat2)= cityhash[loc2]
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    return arc * 3960

print "Distance from CVG to LEX in miles"
print s_distance('CVG','LEX')


# We will now parse each line of our route dataset

def parse_roads(line):
    city1, city2 = line.split(',')
    return city1.strip(), city2.strip()

hiways = map(parse_roads, """
  MKE, CHI 
  MKE, MAD 
  MAD, CHI 
  SEA, BTM 
  SEA, PDX 
  SEA, ALW 
  PDX, SFO 
  PDX, ALW 
  ALW, SLC 
  SFO, SLC 
  SLC, LAX 
  LAX, SAN 
  SAN, TUS 
  LAX, PHX 
  TUS, PHX 
  LAX, FLG 
  FLG, PHX 
  FLG, ABQ 
  ABQ, ELP 
  ELP, DAL 
  ELP, SAT 
  SAT, IAH 
  IAH, DAL 
  DAL, OKC 
  ABQ, OKC 
  ABQ, DEN 
  SLC, DEN 
  DEN, LAX 
  DEN, CYS 
  CYS, SLC 
  CYS, BIL 
  BIL, BTM 
  BIL, FAR 
  OKC, KAN
  DEN, KAN 
  KAN, OMA 
  DEN, OMA 
  OMA, CHI 
  OMA, FAR 
  FAR, MIN 
  MIN, CHI 
  CHI, STL 
  STL, KAN 
  CHI, DET 
  CHI ,IND 
  IND, STL 
  IND, LOU 
  LOU, LEX 
  IND, CVG 
  CVG, LOU 
  CVG, LEX 
  STL, LOU 
  CVG, COL 
  COL, CLE 
  CLE, BUF 
  CLE, PIT 
  CVG, PIT 
  PIT, BUF 
  PIT, PHI 
  PHI, NYC 
  PHI, DCA 
  DCA, ATL 
  ATL, NEW 
  NEW, IAH
  NEW, MEM 
  MEM, OKC 
  MEM, STL 
  MEM, NAS 
  NAS, LOU 
  LEX, KNO 
  NAS, KNO 
  KNO, ATL 
  ATL, TAM 
  ATL, NEW 
  ATL, JAX 
  JAX, MIA 
  JAX, DCA 
  ATL, DCA 
  KNO, DCA 
  DCA, PHI 
  NYC, ALB
  BUF, ALB 
  ALB, BOS 
  NYC, BOS 
  BOS, PRO 
  NYC, PRO 
""".strip().splitlines())

print "Spherical Distance between two cities", hiways[0]
print s_distance(hiways[0][0],hiways[0][1])

#Test road distances
#for e in hiways:
#    print e, s_distance(e[0],e[1])


#Find nearest pair of cities that share a route 
min=1000
minroad = 0
for e in hiways:
    if s_distance(e[0],e[1]) < min :
        min = s_distance(e[0],e[1])
        minroad = e
print minroad, min


#Create the graph using adjacency lists/dicts
G={}
for e in hiways:
 if e[0] in G.keys():
   G[e[0]] = G[e[0]] + [ e[1] ]
 else:
   G[e[0]] =[e[1]]
 
 if e[1] in G.keys():
   G[e[1]]= G[e[1]] + [ e[0] ]
 else:
   G[e[1]] =[e[0]]


#An alternative in which store edges and weights together
##for e  in  hiways:
## if e[0] in G.keys():
##   G[e[0]][e[1]] = s_distance(e[0],e[1])
## else:
##   G[e[0]]={ e[1] : s_distance(e[0],e[1])}
## 
## if e[1] in G.keys():
##   G[e[1]][e[0]] = s_distance(e[0],e[1])
## else:
##   G[e[1]] ={e[0]: s_distance(e[0],e[1])}



def BreadthFirstLevels(G,root):
 visited = set()
 currentLevel = [root]
 visited.add(root)
 while currentLevel:
   nextLevel = set()
   for v in currentLevel:
     for w in G[v]:
        if w not in visited:
           nextLevel.add(w)
           visited.add(w)
   yield nextLevel
   currentLevel = nextLevel


i=1
for l in BreadthFirstLevels(G, 'CVG'):
  print "LEVEL:",i
  print l
  i+=1
 
"""
LEVEL: 1
set(['IND', 'LEX', 'PIT', 'COL', 'LOU'])
LEVEL: 2
set(['KNO', 'PHI', 'STL', 'CHI', 'NAS', 'CLE', 'BUF'])
LEVEL: 3
set(['MKE', 'MIN', 'MEM', 'ALB', 'ATL', 'DET', 'KAN', 'DCA', 'MAD', 'NYC', 'OMA'])
LEVEL: 4
set(['JAX', 'FAR', 'PRO', 'BOS', 'OKC', 'DEN', 'TAM', 'NEW'])
LEVEL: 5
set(['CYS', 'BIL', 'IAH', 'ABQ', 'MIA', 'DAL', 'LAX', 'SLC'])
LEVEL: 6
set(['SAN', 'SFO', 'PHX', 'BTM', 'ALW', 'ELP', 'FLG', 'SAT'])
LEVEL: 7
set(['TUS', 'SEA', 'PDX'])
LEVEL: 8
set([])
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
    print len(citylist)
    for i in sorted_elist:
        print i


#eccentricity(G);

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
      
clustering(G)
##print G

def shortestPath(Graph, source):
  weight = {}

  for v in Graph:
    if v == source:
      weight[v] = 0;
    else:
      weight[v] = float('inf')
  for k in range(1,len(Graph)-1):    
    for i in Graph:
      for j in Graph[i]:
        if weight[i] + s_distance(i,j) < weight[j]:
          weight[j] = weight[i] + s_distance(i,j)

  for i in weight:
    print i, weight[i]

shortestPath(G,'CVG')

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
