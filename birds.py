# Birds
# http://codeforces.com/contest/922/problem/E

n,W,B,X = input("Enter comma separated values of - number of trees, initial points of mana, number of points mana increases when bird is summoned, number of points restored when Imp moves from a tree to next").split(',')

n = int(n)
W = int(W)
B = int(B)
X = int(X)

c = []
for i in range(0,n):
    c.append(int(input()))

cost = []
for i in range(0,n):
    cost.append(int(input()))

# Apply Bubble sort to sort the cost array in increasing order, move the elements of c array in similar order
for i in range(1, len(cost)):
    for j in range(0, i):
        if(cost[j]>cost[j+1]):
            temp=cost[j]
            cost[j]=cost[j+1]
            cost[j+1]=temp

            temp = c[j]
            c[j]=c[j+1]
            c[j+1]=temp

j = 0
birds =0

while W>0:
    while c[j]>0:
        W = W - cost[j] + B
        c[j] = c[j] - 1
        birds = birds + 1
    if c[j] ==0 :
        W = W + X
    j = j + 1

print("Total birds ->  ", birds - 1)