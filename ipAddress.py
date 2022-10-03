# Task: Using Python, get the following outputs in form of individual files from the apache logs (file is attached herewith)
# 	a) LIST OF ALL IP ADDRESSES
# 	b) LIST OF ALL UNIQUE IP ADDRESSES
# 	c) LIST OF IP ADDRESSES & THE VISITED URLS


import re
import csv

def ipAddress():
	pattern = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.+)'
	logfile_path = 'log_file\\apache_logs.txt'
	Contents = open(logfile_path, "r")
	ipList = {}
	urlList = {}

	for line in Contents:
		log_groups = re.match(pattern, line).groups()
		ipList[log_groups[0]] = ipList.get(log_groups[0], 0) + 1
		splittedURL = log_groups[4].split('"')
		subUrl = splittedURL[3].split('+')
		urls = ""
		if splittedURL[1] != '-':
			urls = splittedURL[1]
		elif len(subUrl) >= 2:
			urls = subUrl[1].strip("()")
		else:
			urls = "-"
		urlList[log_groups[0]] = urls

	# print("All IP List:\n",ipList,"\n\n")
	print("All IP and URL:\n",urlList,"\n\n")
	
	# field_names = ['IP', 'URL']
	# with open('IpAddress.csv', 'w') as csvfile:
	# 	writer = csv.DictWriter(csvfile, fieldnames=field_names)
	# 	writer.writeheader()
	# 	writer.writerows(urlList)

	# try:
	# 	geeky_file = open('ipAddress.txt', 'wt')
	# 	geeky_file.write(str(urlList))
	# 	geeky_file.close()

	# except:
	# 	print("Unable to write to file")

def main():
	ipAddress()

if __name__ == "__main__":
	main()
