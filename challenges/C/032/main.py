import math

N = int(input())

p0 = 0
p1 = 0
p2 = 0
p3 = 0
for i in range(N):
  v_n, p_n = map(int, input().split())
  
  if v_n == 0:
    p0 += p_n
  elif v_n == 1:
    p1 += p_n
  elif v_n == 2:
    p2 += p_n
  else:
    p3 += p_n

x0 = math.floor(p0 / 100) * 5
x1 = math.floor(p1 / 100) * 3
x2 = math.floor(p2 / 100) * 2
x3 = math.floor(p3 / 100) * 1

ans = [x0, x1, x2, x3]
print(sum(ans))
