#Given a list of intervals: [s, e] for meeting
#Find the least number of rooms required

A = list((list((1, 10)), list((15, 20)), list((0, 30))))

data = []

for s, e in A:        #create a touple based on list: [(1, 1), (10, -1), (15, 1), (20, -1), (0, 1), (30, -1)]
  data.append((s, 1))
  data.append((e, -1))

data.sort()           #sort it: [(0, 1), (1, 1), (10, -1), (15, 1), (20, -1), (30, -1)]

curr = 0
ans = 0

for _, v in data:
  curr += v
  ans = max(ans, curr)

print("Meeting rooms required: ", ans)