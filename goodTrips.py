n = int(input())
i = []
li = []
for _ in range(n):
    i = list(map(int,input().split()))
    li.append(i)
maxNum = 0

for i in range(n):
	colMax = 0
	for j in range(n):
		if(colMax < li[j][i]):
			colMax = li[j][i]
			# print(colMax)
	maxNum+=colMax

print(maxNum)