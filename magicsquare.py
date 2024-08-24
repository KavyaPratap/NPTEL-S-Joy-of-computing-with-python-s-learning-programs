def magic_square(n):
    # Initialize an n x n matrix with zeros
    magicsquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicsquare.append(l)
  
    # Start position
    i = n // 2
    j = n - 1
  
    # Fill the matrix with numbers from 1 to n*n
    num = n * n 
    count = 1 
  
    while count <= num:
        # Wrap around if out of bounds
        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
        
        # If cell is already filled, move to the next position
        if magicsquare[i][j] != 0:
            j = j - 2
            i = i + 1 
            continue
        else:
            magicsquare[i][j] = count
            count += 1 
        i = i - 1
        j = j + 1 
    
    # Print the magic square
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j], end=" ")
        print()

# Example usage
magic_square(5)
