def kp(n):
  #initializing matrix of order nxn initially filled with zeroes..(0)
  ms=[]
  for i in range(n):
    l=[]
    for j in range(n):
      l.append(0)
    ms.append(l)

  i=n//2 # i is initialized to the middle row
  j=n-1 # j is initialized to the last column

  # placing numbers from 1 to n^2 
  
  num=n*n 
  count=1 
  
  while (count<=num):
    if (i==-1 and j==n):
      i=0
      j=n-2
    else:
      if (j==n):
        j=0
      if (i<0):
        i=n-1
        
    if (ms[i][j]!=0) :
      j=j-2
      i=i+1 
      continue
    else:
      ms[i][j]=count
      count+=1 
    i=i-1
    j=j+1 
    # printing the magic square...
  for i in range(n):
    for j in range(n):
      print(ms[i][j],end=" ")
    print()

kp(5)
