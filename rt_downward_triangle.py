'''Right Triangle Star Pattern'''
N=5 #Nuumber of rows
for i in range(N): #loop for rows
    for j in range(i,N):    #loop that runs inside a row
        print("*", end=" ")
    print()
