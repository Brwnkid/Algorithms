def longest_pal(str):
  n=len(str)
  #initialize Opt Table
  Opt=[[0 for i in  range(n)] for j in  range(n)  ]
  #initializes table for values that are too close
  for i in  range(n):
    for j in range(i-5,i+6):
      if j < n and j > 0:
        Opt[i][j] = 0
  # define  sil as  length  of  substring interval  [i,j]   sil=(j-i  +1)
  # compute Opt table entry for each  starting  index i and each  sil
  for sil in  range(6,  n+1):
    for i in  range(n-sil+1):
      j = i+sil-1
      if (str[i] ==  str[j]  and sil ==  6):
        Opt[i][j] = 2
      elif  (str[i] ==  str[j]):
        Opt[i][j] = Opt[i+1][j-1] + 2;
      else:
        Opt[i][j] = max(Opt[i][j-1],  Opt[i+1][j])
  return  Opt[0][n-1]

str1="racecar"
str2="abccccba"
str3="a man a plan a canal panama"
str4="a man two cats a crazy plan aibohphobia and a canal in panama"
print str1,"has longest palindrome substring length:"
print longest_pal(str1)
print str2,"has longest palindrome substring length:"
print longest_pal(str2)
print str3,"has longest palindrome substring length:"
print longest_pal(str3)
print str4,"has longest palindrome substring length:"
print longest_pal(str4)
