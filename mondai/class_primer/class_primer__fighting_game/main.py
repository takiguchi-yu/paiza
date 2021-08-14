# プレイヤークラス
class Player:
  def __init__(self, hp, f1, a1, f2, a2, f3, a3) -> None:
    self.hp = hp
    # フレーム
    self.frame = [f1, f2, f3]
    # 技
    self.attack = [a1, a2, a3]
    # 生死
    self.alive = True

  # ダメージを受ける
  def take_damage(self, damage) -> None:
    self.hp -= damage
    if self.hp <= 0:
      self.alive = False

  # ステータス強化
  def enhance_status(self):
    for i in range(3):
      if self.frame[i] == 0 and self.attack[i] == 0:
        continue

      self.frame[i] = max(self.frame[i]-3, 1)
      self.attack[i] += 5

  # ステータス取得
  def get_status(self, i):
    return [self.frame[i], self.attack[i]]

  def get_alive(self):
    return self.alive

N, K = map(int, input().split())

players = [None] * N
for i in range(N):
  # HP、フレーム1、攻撃力1、フレーム2、攻撃力2、フレーム3、攻撃力3
  hp, f1, a1, f2, a2, f3, a3 = map(int, input().split())
  
  players[i] = Player(hp, f1, a1, f2, a2, f3, a3)

for _ in range(K):
  # プレイヤー1、技1、プレイヤー2、技2
  p1, t1, p2, t2 = map(int, input().split())
  # プレイヤー1
  p1_i = p1 - 1
  t1_i = t1 - 1
  # プレイヤー2
  p2_i = p2 - 1
  t2_i = t2 - 1

  # プレイヤーが死んでいればスキップ
  if not players[p1_i].get_alive() or not players[p2_i].get_alive():
    continue

  # プレイヤーのフレームを取得
  p1_f, p1_a = players[p1_i].get_status(t1_i)
  p2_f, p2_a = players[p2_i].get_status(t2_i)

  # 強化するか判定
  if p1_f == 0 and p1_a == 0 and p2_f == 0 and p2_a == 0:
    # プレイヤーが２人とも強化ならそのまま強化
    players[p1_i].enhance_status()
    players[p2_i].enhance_status()
  elif p1_f == 0 and p1_a == 0:
    players[p1_i].enhance_status()
    players[p1_i].take_damage(p2_a) # 相手が強化ではない場合はそのままダメージを受ける
  elif p2_f == 0 and p2_a == 0:
    players[p2_i].enhance_status()
    players[p2_i].take_damage(p1_a) # 相手が強化ではない場合はそのままダメージを受ける
  else:
    # プレイヤー1が攻撃
    if p1_f < p2_f:
      players[p2_i].take_damage(p1_a)
    # プレイヤー2が攻撃
    elif p1_f > p2_f:
      players[p1_i].take_damage(p2_a)
    else:
      pass  # 同じの場合は何も起こらない

p_num = 0
for player in players:
  if player.get_alive():
    p_num += 1
    
print(p_num)
