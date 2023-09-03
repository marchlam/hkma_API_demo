import urllib.request
import json
url = 'https://api.hkma.gov.hk/public/bank-svf-info/hotlines-report-loss-credit-card?lang=en&offset=0'
output_file_name = 'hotline.json'
response = urllib.request.urlopen(url)
#print (req.read())
data_json = json.loads(response.read())

with open(output_file_name, 'w') as json_file:
  json.dump(data_json, json_file)