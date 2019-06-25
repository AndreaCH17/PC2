import random
N =[]
estado = True
while estado == True:
        x = int (input("Ingrese numero entre 1 y 10:"))
        while x > 10:
            x = int (input ("Ingrese un numero entre 1 y 10:"))
        if x < 10:    
            N.append (x)
        if len(N) == 6:
         estado = False
         print (N)


M = []
A =[]
for i in range (1,10):

    M.append (i)
print (M)
    
c = random.choice(M)

while len(A)< 6:
    A.append(c)
print (A)

cont = 0
for i in N:
    for j in A:
        if i == j:
            cont = cont +1 
print (cont)

if cont == 6:
    print ("Ha ganado 6 millones de soles")
elif cont == 5:
    print ("Ha ganado 100 mil soles")
elif cont == 4:
    print ("Siga intentado")