import urllib2
import sys
import datetime
import time

url1 = 'https://ws.webtrends.com/v3/Reporting/spaces/Keymetrics/?start_period=current_day-28&end_period=current_day-1&language=en-US&suppress_error_codes=true&format=html'
url2 = 'https://ws.webtrends.com/v3/Reporting/spaces/Keymetrics/?start_period=current_day-56&end_period=current_day-29&language=en-US&suppress_error_codes=true&format=html'

filename = 'FIVE_TWITTER_request_times.txt'

f = open(filename, 'w')
now = datetime.datetime.now()
f.write("Starting Collection Process on --> " + now.strftime("%Y-%m-%d") + " at " + now.strftime("%H:%M:%S") + "\n\n")
f.close()

timelist = []

for n in range(1, 51):
	
	#Get FB Report Data
	f = open(filename, 'a')
	
	f.write("FIVE_TWITTER FirstRequest " + str(n))
	nowStart = datetime.datetime.now()
	strStartTime = nowStart.strftime("%H:%M:%S-%f")
	f.write(" ___ Start Time ||||| " + strStartTime + " ||||| ")


	passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
	passman.add_password(None, url1, 'FIVE_TWITTER\olsena', 'Intern@1')
	urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))


	req = urllib2.Request(url1)
	response = urllib2.urlopen(req)

	html = response.read()
	
	#write it out to file - debug purposes
	#f1 = open('FIVE_TWITTER_OUT1.html', 'w')
	#f1.write(html)
	#f1.close()
	
	nowEnd = datetime.datetime.now()
	strEndTime = nowEnd.strftime("%H:%M:%S-%f")
	
	timeDiff = nowEnd - nowStart
	
	timelist.append(timeDiff)
	
	
	f.write("End Time ||||| " + strEndTime + " ------  Difference is " + str(timeDiff.seconds) + "." + str(timeDiff.microseconds) + "\n")
	
	f.close()
	
	
	#Round 2
	f = open(filename, 'a')
	
	f.write("FIVE_TWITTER SecondRequest " + str(n))
	nowStart = datetime.datetime.now()
	strStartTime = nowStart.strftime("%H:%M:%S-%f")
	f.write(" ___ Start Time ||||| " + strStartTime + " ||||| ")


	passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
	passman.add_password(None, url2, 'FIVE_TWITTER\olsena', 'Intern@1')
	urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))

	req = urllib2.Request(url2)
	response = urllib2.urlopen(req)

	html = response.read()
	
	#write it out to file - debug purposes
	#f1 = open('FIVE_TWITTER_OUT2.html', 'w')
	#f1.write(html)
	#f1.close()
	
	nowEnd = datetime.datetime.now()
	strEndTime = nowEnd.strftime("%H:%M:%S-%f")
	
	timeDiff = nowEnd - nowStart
	
	timelist.append(timeDiff)
	
	
	f.write("End Time ||||| " + strEndTime + " ------  Difference is " + str(timeDiff.seconds) + "." + str(timeDiff.microseconds) + "\n")
	
	f.close()
	
	
	time.sleep(10)
	
avgTime = sum(timelist, datetime.timedelta(0)) / len(timelist)

f = open(filename, 'a')

f.write("\nCollected " + str(n) + " records\n")
f.write("The Average response time was " + str(avgTime))
	
#f1.close()
f.close()