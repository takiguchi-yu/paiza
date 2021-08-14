H, W = map(int, input().split())
dy, dx = map(int, input().split())

# 描画する画素数は (30 × 240) + (30 × 180) - (30 × 30) = 11700 画素となります。
ans = abs(H * dx) + abs(W * dy) - abs(dy * dx)

print(ans)
