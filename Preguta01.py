A = [[1,2,3],[2,4,6],[5,3,1]]
print (A)

i = 0
j = 0
suma = 0
while i <= len (A) and j <= len (A):
    i = i+1 
    j = j+1
    suma = suma + A[i,j]

    if suma / 2 == 0:
        print ("La diagonal es par")
    else:
        print ("La diagonal es impar")