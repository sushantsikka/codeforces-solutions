# Cheap travel
# http://codeforces.com/problemset/problem/466/A

n = int(input("Enter number of rides planned"))
m = int(input("Enter number of rides covered by m ticket"))
a = int(input("Enter price of one ticket"))
b = int(input("Enter price of m ride ticket"))

sum1 = ((n-(m*int((n/m))))*a) + (b*int((n/m)))
sum2 = n * a

if (sum1<sum2):
    print("Min cost ->", sum1)
else:
    print("Min cost ->", sum2)