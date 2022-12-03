'''Right Triangle Star Pattern'''
N=5 #Number of rows we want
for i in range(N):  #loop for rows
    for j in range(i+1): #loop to run Inside a row 
        print("*", end=" ")
    print()
