# Task: Using Python, get the following outputs in form of individual files from the apache logs (file is attached herewith)
# 	a) LIST OF ALL IP ADDRESSES
# 	b) LIST OF ALL UNIQUE IP ADDRESSES
# 	c) LIST OF IP ADDRESSES & THE VISITED URLS

# def ipAddress(logfile_path):
# 	ipList = {}
# 	Contents = open(logfile_path, "r")
# 	# You can use .readlines in old Python, but if the log is huge...

# 	# Go through each line of the logfile
# 	for line in Contents:
# 		# Split the string to isolate the IP address
# 		Ip = line.split(" ")[0]

# 		if 6 < len(Ip) <= 15:
# 			# Increase by 1 if IP exists; else set hit count = 1
# 			ipList[Ip] = ipList.get(Ip, 0) + 1

# 	print("All the IPs: ",ipList)

# ipAddress('log_file\\apache_logs.txt')
import re
import csv

# [(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) (.+)
# def printAllIp():


def ipAddress():
	pattern = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.+)'
	logfile_path = 'log_file\\apache_logs_2.txt'
	urlPatterm = '^(http[s]?:\\/\\/(www\\.)?|ftp:\\/\\/(www\\.)?|www\\.){1}([0-9A-Za-z-\\.@:%_\+~#=]+)+((\\.[a-zA-Z]{2,3})+)(/(.)*)?(\\?(.)*)?'
	Contents = open(logfile_path, "r")
	ipList = {}
	urlList = {}

	for line in Contents:
		log_groups = re.match(pattern, line).groups()
		ipList[log_groups[0]] = ipList.get(log_groups[0], 0) + 1
		splittedURL = log_groups[4].split('"')
		# urls = re.match(urlPatterm, splittedURL)
		print(splittedURL)
		# urlList[log_groups[0]] = log_groups[4]
		# print(urls)

	# print(ipList)
	# print(urlList)
	# print(log_groups[4])

def main():
	ipAddress()

if __name__ == "__main__":
	main()
