N, A, B = map(int, input().split())

s_N = list(input())
s_A = list(input())
s_B = list(input())

j = 0
a_match = 0
for s in s_A:
  for n in range(j, len(s_N)):
    j += 1
    # print(s, s_N[n])
    if s == s_N[n]:
      a_match += 1
      break
j = 0
b_match = 0
for s in s_B:
  for n in range(j, len(s_N)):
    j += 1
    # print(s, s_N[n])
    if s == s_N[n]:
      b_match += 1
      break


a_not_match = len(s_A) - a_match
b_not_match = len(s_B) - b_match
print(a_not_match, b_not_match)
