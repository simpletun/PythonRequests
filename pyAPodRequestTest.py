import sys
import datetime
import requests

url = 'https://adx.webtrends.com/v3/Reporting/profiles/60856/Keymetrics/?start_period=2013m04d12&end_period=2013m05d16&language=en-US&format=html&suppress_error_codes=true'

filename = 'DashRequest_times.txt'

f = open(filename, 'w')
now = datetime.datetime.now()
f.write("Starting Collection Process on --> " + now.strftime("%Y-%m-%d") + " at " + now.strftime("%H:%M:%S") + "\n\n")
f.close()

timelist = []

for n in range(1, 6):
	
	#Getting Dashboard Data
	f = open(filename, 'a')
	
	f.write("Dashboard Pass " + str(n))
	nowStart = datetime.datetime.now()
	strStartTime = nowStart.strftime("%H:%M:%S-%f")
	f.write(" ___ Start Time ||||| " + strStartTime + " ||||| ")

	#Perform request
	req = requests.get(url, auth=('motorcycleusa\olsena', 'intern@l'), verify=False)

	#write it out to file - debug purposes
	f1 = open('Dash_output.html', 'w')
	f1.write(req.text)
	f1.close()
	
	nowEnd = datetime.datetime.now()
	strEndTime = nowEnd.strftime("%H:%M:%S-%f")
	
	timeDiff = nowEnd - nowStart
	
	timelist.append(timeDiff)
	
	
	f.write("End Time ||||| " + strEndTime + " ------  Difference is " + str(timeDiff.seconds) + "." + str(timeDiff.microseconds) + "\n")
	
	f.close()
	
	
avgTime = sum(timelist, datetime.timedelta(0)) / len(timelist)

f = open(filename, 'a')

f.write("\nCollected " + str(n) + " records\n")
f.write("The Average response time was " + str(avgTime))
	
#f1.close()
f.close()