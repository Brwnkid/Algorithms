def Edit_distance(str1,str2):
  CONST_DEL = 3
  CONST_INS = 4
  CONST_REP = 5
  #initializes table
  table = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

  #sets base conditions for table, inserting all letters left in a string
  for i in range(1,len(str1)+1):
    table[i][0] = i*CONST_DEL
  for j in range(1,len(str2)+1):
    table[0][j] = j*CONST_INS
  #loops over table and enters 
  for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
      if str1[i-1] == str2[j-1]:
        table[i][j] = table[i-1][j-1] #if character is the same, no change
      else:
        table[i][j] = min(table[i-1][j]+CONST_DEL,  #delete character
                          table[i][j-1]+CONST_INS,  #insert character
                          table[i-1][j-1]+CONST_REP)#repalce character
##  testing table
##  for i in table:
##    print i
  print table[len(str1)][len(str2)]


Low_Cost_Genome_Edit(a[0..m],b[0..n]):
  Table = [m+1][n+1]
  for i in range(m+2):
    Table[i][0] = i*$3 #delete all letters that are in a, when b is an empty string.
  for j in range(n+2):
    Table[0][j] = j*$4 #insert all letters that are in b, when a is an empty string.
  for i from 1 to m+1:  
    for j from 1 to n+1:
      if a[i-1] == b[j-1]:
        Table[i][j] = Table [i-1][j-1]
      else:
        table[i][j] = min(Table[i-1][j]+$3,Table[i][j-1]+$4,Table[i-1][j-1]+$5)

  return Table[m][n]
  
