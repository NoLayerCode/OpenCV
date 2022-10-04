# Task: Using Python, get the following outputs in form of individual files from the apache logs (file is attached herewith)
# 	a) LIST OF ALL IP ADDRESSES
# 	b) LIST OF ALL UNIQUE IP ADDRESSES
# 	c) LIST OF IP ADDRESSES & THE VISITED URLS

import re

def ipAddress():
	pattern = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.+)'
	logfile_path = 'log_file\\apache_logs.txt'
	Contents = open(logfile_path, "r")
	ipList = dict()
	uniqueIpList = set()
	urlList = list()

	for line in Contents:
		log_groups = re.match(pattern, line).groups()
		ipList[log_groups[0]] = ipList.get(log_groups[0], 0) + 1
		splittedURL = log_groups[4].split('"')
		urls = ""
		if splittedURL[1] != '-':
			urls = splittedURL[1]
		else:
			urls = "-"
		urlList.append((log_groups[0], urls))

	for value in ipList:
		key = ipList[value]
		if key == 1:
			uniqueIpList.add(value)

	print("All IP List:\n",ipList,"\n\n")
	print("All Unique IP List:\n",uniqueIpList,"\n\n")
	print("All IP and URL:\n",urlList)
	

def main():
	ipAddress()

if __name__ == "__main__":
	main()
