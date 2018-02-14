# Vasya The Hipster
# http://codeforces.com/problemset/problem/581/A

a,b = input("Enter number of red and blue socks").split(',')
a = int(a)
b = int(b)

d1=0
d2=0

if a>b:
    d1 = b
    d2 = int((a-b)/2)
else:
    d1 = a
    d2 = int((b - a) / 2)

print(d1,d2)
