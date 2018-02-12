# Cheap travel
# http://codeforces.com/problemset/problem/466/A

n = int(input("Enter number of rides planned"))
m = int(input("Enter number of rides covered by m ticket"))
a = int(input("Enter price of one ticket"))
b = int(input("Enter price of m ride ticket"))

sum1 = ((n-(m*(n/m)))*a) + (b*(n/m))
sum2 = int(n) * int(a)

if (sum1<sum2):
    print("Min cost ->", sum1)
else:
    print("Min cost ->", sum2)