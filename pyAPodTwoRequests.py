import datetime
import time
import requests

url = 'https://adx.webtrends.com/v3/Reporting/profiles/60856/Keymetrics/?start_period=2013m04d12&end_period=2013m05d16&language=en-US&format=html&suppress_error_codes=true'
url2 = 'https://adx.webtrends.com/v3/Reporting/profiles/60856/reports/18d039ae036/?start_period=2013m04d12&end_period=2013m05d16&language=en-US&format=html&suppress_error_codes=true'

filename = 'Request_times.txt'

f = open(filename, 'w')
now = datetime.datetime.now()
f.write("Starting Collection Process on --> " + now.strftime("%Y-%m-%d") + " at " + now.strftime("%H:%M:%S") + "\n\n")
f.close()

timelist = []
timelist2 = []

for n in range(1, 6):
	
	#Getting Dashboard Data
	f = open(filename, 'a')
	
	f.write("Key Metrics Request" + str(n))
	nowStart = datetime.datetime.now()
	strStartTime = nowStart.strftime("%H:%M:%S-%f")
	f.write(" ___ Start Time ||||| " + strStartTime + " ||||| ")


	#Perform request
	req = requests.get(url, auth=('motorcycleusa\olsena', 'intern@l'), verify=False)

	#write it out to file - debug purposes
	f1 = open('dash_output.html', 'w')
	f1.write(req.text)
	f1.close()
	
	nowEnd = datetime.datetime.now()
	strEndTime = nowEnd.strftime("%H:%M:%S-%f")
	
	timeDiff = nowEnd - nowStart
	
	timelist.append(timeDiff)
	
	
	f.write("End Time ||||| " + strEndTime + " ------  Difference is " + str(timeDiff.seconds) + "." + str(timeDiff.microseconds) + "\n")
	
	f.close()
	
	#Second report
	f = open(filename, 'a')
	
	f.write("Report Request" + str(n))
	nowStart = datetime.datetime.now()
	strStartTime = nowStart.strftime("%H:%M:%S-%f")
	f.write(" ___ Start Time ||||| " + strStartTime + " ||||| ")


	#Perform request
	req = requests.get(url2, auth=('motorcycleusa\olsena', 'intern@l'), verify=False)

	#write it out to file - debug purposes
	f1 = open('report_output.html', 'w')
	f1.write(req.text)
	f1.close()
	
	nowEnd = datetime.datetime.now()
	strEndTime = nowEnd.strftime("%H:%M:%S-%f")
	
	timeDiff = nowEnd - nowStart
	
	timelist2.append(timeDiff)
	
	
	f.write("End Time ||||| " + strEndTime + " ------  Difference is " + str(timeDiff.seconds) + "." + str(timeDiff.microseconds) + "\n")
	
	f.close()
	
	time.sleep(5)
	
#Requests done, now figure out the average	
avgTime = sum(timelist, datetime.timedelta(0)) / len(timelist)
avgTime2 = sum(timelist2, datetime.timedelta(0)) / len(timelist2)

f = open(filename, 'a')

f.write("\nExtracted " + str(n) + " reports\n")
f.write("The Average response time for FIRST REQUEST was " + str(avgTime) + "\n")
f.write("The Average response time for SECOND REQUEST was " + str(avgTime2))
	
#f1.close()
f.close()