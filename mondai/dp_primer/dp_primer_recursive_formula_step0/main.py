x, d, k = map(int, input().split())

a = [x] * (k + 1)
for i in range(2, k + 1):
  a[i] = a[i-1] + d
  # print(a)

print(a[k])
