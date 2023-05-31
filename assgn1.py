from numpy import*
n=int(input("Enter n: "))
M1=[]
print("For Markov chain matrix Mnxn: ")
for i in range(0,n):#for creating inner list
    M1.append([])#for adding list to matrix
for i in range(0,n):#for row
    for j in range(0,n):#for coloumn
        M1[i].append(j)#will add elements to the list
        M1[i][j]=0
for i in range(0,n):
    for j in range(0,n):
        print("Enter the value in row ",(i+1) , " coloumn " ,(j+1))
        M1[i][j]=float(input())
M2=[]
print("For current state: ")
for i in range(0,1):#for creating inner list
    M2.append([])#for adding list to matrix
for i in range(0,1):#for row
    for j in range(0,n):#for coloumn
        M2[i].append(j)#will add elements to the list
        M2[i][j]=0
for i in range(0,1):
    for j in range(0,n):
        print("Enter the value in row ",(i+1) , " coloumn " ,(j+1))
        M2[i][j]=float(input())

m1=matrix(M1)
m2=matrix(M2)
time=int(input("Enter time: (assuming each transition takes unit time)"))
for i in range(0,time):
    m2=m2*m1
print(m2)
