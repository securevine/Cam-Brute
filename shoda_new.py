import shodan
import time
SHODAN_API_KEY = "********************************"
api = shodan.Shodan(SHODAN_API_KEY)
page=1
while page ==1 or results['matches']:
	try:
		results = api.search("country:SA port:'554'",page=page)
		for result in results['matches']:
			print ('%s' % (result['ip_str']))	
		page+=1	
		time.sleep(0.5)	
	except shodan.APIError:
		continue







