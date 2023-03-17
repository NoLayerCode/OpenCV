import math

li = []

t = int(input())
li = list(map(int, input().split()))

distance = 0

for i in li:
	distance += math.dist((li[0], 0), (i, 0))

print(distance*2)