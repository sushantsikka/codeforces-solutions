# Young Physicist
# http://codeforces.com/problemset/problem/69/A

n = int(input("Enter the number of force vectors applied on the body"))

x_arr = []
y_arr = []
z_arr = []

for i in range(n):
    x,y,z = input().split(',')
    x_arr.append(int(x))
    y_arr.append(int(y))
    z_arr.append(int(z))

# Sum the x, y and z coordinates of all the force vectors

for i in range(1,n):
    x_arr[0]= x_arr[0] + x_arr[i]
    y_arr[0] = y_arr[0] + y_arr[i]
    z_arr[0] = z_arr[0] + z_arr[i]


if(x_arr[0]==0 and y_arr[0]==0 and z_arr[0]==0):
    print("YES")
else:
    print("NO")