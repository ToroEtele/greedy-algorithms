# Given a list of intervals
# [[1,2],[2,10],[4,6]]
# Find the length of the maximal set of mutually disjoint intervalls

A = list((list((8,11)), list((9,12)), list((1,2)), list((3,5)), list((1,3)), list((4,6)), list((6,7))))

A.sort(key=lambda x: x[1]) #végpont szerint növekvő sorrendbe rendezzük.

prev_s, prev_e = A[0]
count = 1

for s, e in A:
  if s <= prev_e: #ha hamarább kezdődik mint az előző vége akkor nem jó
    pass
  else:
    prev_e, prev_s = s, e
    count += 1

print(A)