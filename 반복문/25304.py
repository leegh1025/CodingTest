x = int(input())

n = int(input())

sum = 0
for i in range(n):
    a , b = map(int , input().split())
    num = a * b
    sum += num

if x == sum :
    print("Yes")
else:
    print("No")