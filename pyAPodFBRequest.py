import urllib2
import sys
import datetime

url = 'https://adx.webtrends.com/v3/Reporting/profiles/50488/reports/FacebookPostKeyMetrics/?totals=all&start_period=current_day-28&end_period=current_day&period_type=agg&format=html&suppress_error_codes=true'

filename = 'FBrequest_times.txt'

f = open(filename, 'w')
now = datetime.datetime.now()
f.write("Starting Collection Process on --> " + now.strftime("%Y-%m-%d") + " at " + now.strftime("%H:%M:%S") + "\n\n")
f.close()

timelist = []

for n in range(1, 6):
	
	#Get FB Report Data
	f = open(filename, 'a')
	
	f.write("Facebook Pass " + str(n))
	nowStart = datetime.datetime.now()
	strStartTime = nowStart.strftime("%H:%M:%S-%f")
	f.write(" ___ Start Time ||||| " + strStartTime + " ||||| ")


	passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
	passman.add_password(None, url, 'webtrends_com\olsena', 'intern@l')
	urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))


	req = urllib2.Request(url)
	response = urllib2.urlopen(req)

	html = response.read()
	
	#write it out to file - debug purposes
	#f1 = open('Facebook_output.html', 'w')
	#f1.write(html)
	#f1.close()
	
	nowEnd = datetime.datetime.now()
	strEndTime = nowEnd.strftime("%H:%M:%S-%f")
	
	timeDiff = nowEnd - nowStart
	
	timelist.append(timeDiff)
	
	
	f.write("End Time ||||| " + strEndTime + " ------  Difference is " + str(timeDiff.seconds) + "." + str(timeDiff.microseconds) + "\n")
	
	f.close()
	

	#f1.write(html)
	
avgTime = sum(timelist, datetime.timedelta(0)) / len(timelist)

f = open(filename, 'a')

f.write("\nCollected " + str(n) + " records\n")
f.write("The Average response time was " + str(avgTime))
	
#f1.close()
f.close()