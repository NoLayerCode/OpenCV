# 5
# 5
# apple
# 15
# schtschurowskia
# 6
# polish
# 5
# tryst
# 3
# cry

# cook your dish here
for _ in range(int(input())):
	n = int(input())
	s = input()
	if n<=3:
		print("YES")
	else:
		for i in range(n-3):
			string = s[i:i+4]
			print(string)
			vow1 = 'a' in string or 'e' in string or 'i' in string 
			vow2 = 'o' in string or 'u' in string 
			if not vow1 and not vow2:
				print("NO")
				break 
		else:
			print("YES")