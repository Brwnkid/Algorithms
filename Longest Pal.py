def longest_pal(str):
  n=len(str)
  #initialize Opt Table
  Opt=[[0 for i in  range(n)] for j in  range(n)  ]
  for i in  range(n):
    Opt[i][i] = 1
  # define  sil as  length  of  substring interval  [i,j]   sil=(j-i  +1)
  # compute Opt table entry for each  starting  index i and each  sil
  for sil in  range(2,  n+1):
    for i in  range(n-sil+1):
      j = i+sil-1
      if (str[i] ==  str[j]  and sil ==  2):
        Opt[i][j] = 2
      elif  (str[i] ==  str[j]):
        Opt[i][j] = Opt[i+1][j-1] + 2;
      else:
        Opt[i][j] = max(Opt[i][j-1],  Opt[i+1][j])
  return  Opt[0][n-1]

str1="aibohphobia"
print str1,"has longest palindrome substring length:"
print longest_pal(str1)
 
