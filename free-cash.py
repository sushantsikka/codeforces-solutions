# Free Cash
# http://codeforces.com/problemset/problem/237/A

n = int(input("Enter number of incoming customers"))
matrix=[]
hr = []
mm = []

for i in range(0,n):
    hr_val,mm_val = input("Enter time of entry (hr,mm)").split(',')
    hr.append(hr_val)
    mm.append(mm_val)

k = 0
cash = 0
if len(hr) > 0:
    cash = 1
    while k<n-1:
        if((int(hr[k+1])-int(hr[k]))*60 + (int(mm[k+1])-int(mm[k])) < 1):
            cash= cash+1
        k=k+1

print("Min cash required -> ", cash)


