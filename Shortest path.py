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

##OUTPUT:
##MKE 337.655612618
##MIN 616.783786926
##MIA 993.784462683
##ATL 389.226283127
##BOS 793.516576232
##DET 503.857707802
##NAS 235.71417318
##DEN 1105.75942158
##LOU 80.7376884554
##NEW 779.198418723
##COL 110.682018467
##FLG 1651.91485121
##CYS 1202.55619795
##BIL 1396.71726488
##SAN 2063.28459289
##SFO 2085.12985715
##DAL 1034.71418588
##PRO 756.573555606
##BTM 1588.01364906
##DCA 646.961509748
##SEA 2063.61569639
##CHI 263.97263641
##TAM 798.649426991
##BUF 417.659936634
##SAT 1287.29211681
##KNO 226.583082055
##CVG 0
##IAH 1097.62739491
##JAX 658.964633019
##PDX 2182.52562268
##STL 327.192843892
##CLE 225.953840133
##OMA 692.20990126
##ABQ 1367.41495027
##ELP 1588.15650154
##IND 97.5321678029
##SLC 1486.80032057
##LAX 1954.0906099
##PHI 521.024528907
##MEM 432.236529302
##PIT 267.55132218
##TUS 1886.7537084
##ALB 667.780834989
##KAN 554.238485994
##FAR 832.520848493
##OKC 858.878807871
##PHX 1776.25743247
##NYC 605.129694834
##MAD 384.362688072
##LEX 71.3795069621
##ALW 1971.73122265