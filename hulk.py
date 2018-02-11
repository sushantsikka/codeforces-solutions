# Hulk problem
# http://codeforces.com/problemset/problem/705/A

n=input("Enter value of n")
n=int(n)
i=1
a=''

while i<=n:
    if i%2==1 and i!=n:
        a=a+"I hate that "
    if i%2==1 and i==n:
        a=a+"I hate "
    if i%2==0 and i!=n:
        a=a+"I love that "
    if i%2==0 and i==n:
        a=a+"I love "
    i=i+1

a=a+"it"
print(a)
