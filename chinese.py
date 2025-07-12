n = int(input())
day= list(map(int, input().split()))
night= list(map(int, input().split()))
x = int(input())
day.sort()                   
night.sort(reverse=True)     
pay = 0

for i in range(n):
    total = day[i] + night[i]
    if total > x:
        pay += (total - x) * 100
print(pay)
