import json
f = open('hotline.json')
d = json.load(f)

print(json.dumps(d , indent= 4 ,sort_keys=True))