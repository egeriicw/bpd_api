Buildings Performance Database API Access

Add a file called config.py which contains the following:

BPD_API_KEY = 'ApiKey'

BPD_API_USERNAME = 'email address'

BPD_API_BASEURL = 'https://bpd.lbl.gov/api/v1/analyze'

BPD_API_HEADERS = {'Content-Type': 'application/json','Authorization': 'ApiKey %s:%s'% (BPD_API_USERNAME, BPD_API_KEY)}
