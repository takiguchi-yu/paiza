def reverse_num(n):
  r = list(str(n))
  r.reverse()
  r = int("".join(r))  
  return r

n = int(input())

for i in range(1000):
  r = reverse_num(n)
  a = n + r

  n_array = list(str(a))
  r_array = list(str(reverse_num(a)))

  if n_array == r_array:
    print("".join(n_array))
    break

  n = a
