# Business trip
# http://codeforces.com/problemset/problem/149/A

k = input("Enter k")

k = int(k)
a = list()

i=1
for i in range(12):
    val = input()
    a.append(int(val))

a.sort(reverse=True)

i = 0
val = 0
while k>0 and i<12:
    k = k - a[i]
    i = i + 1

if i != 12:
    print(i)
if i == 12:
    print("-1")


