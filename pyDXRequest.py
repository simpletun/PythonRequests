import urllib2
import sys
from datetime import datetime

url = 'https://adx.webtrends.com/v3/Reporting/profiles/60856/Keymetrics/?start_period=2013m05d01&end_period=2013m05d15&language=en-US&format=html&suppress_error_codes=true'

f = open('request_times.txt', 'w')
now = datetime.now()
f.write("Starting Collection Process on --> " + now.strftime("%Y-%m-%d") + "\n\n")
f.close()

for n in range(1, 6):
	
	f = open('request_times.txt', 'a')
	
	f.write("Pass " + str(n))
	nowStart = datetime.now()
	strStartTime = nowStart.strftime("%H:%M:%S-%f")
	f.write(" ___ My Start Time ||||| " + strStartTime + " ||||| ")


	passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
	passman.add_password(None, url, 'motorcycleusa\olsena', 'intern@l')
	urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))


	req = urllib2.Request(url)
	response = urllib2.urlopen(req)

	html = response.read()
	
	outfile = open('output' + str(n) + '.html', 'w')
	outfile.write(html)
	outfile.close()
	
	nowEnd = datetime.now()
	strEndTime = nowEnd.strftime("%H:%M:%S-%f")
	
	timeDiff = nowEnd - nowStart
	
	
	f.write("My End Time ||||| " + strEndTime + " ------  Difference is " + str(timeDiff.seconds) + "." + str(timeDiff.microseconds) + "\n")
	
	f.close()

	#f1.write(html)

f = open('request_times.txt', 'a')

f.write("\nCollected " + str(n) + " records out")
	
#f1.close()
f.close()