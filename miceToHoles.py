#There are N mice and N holes. A mice takes 1 minute to travel 1 unit left or right.
#Find the minimum time after which all mice are in holes.

mice = [3, 2, -4]
hole = [0, -2, 4]

mice.sort()
hole.sort()

ans = 0

for a,b in zip(mice, hole):
  ans = max(ans, abs(a-b))
