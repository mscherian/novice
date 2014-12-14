import json

output = open('breaches.txt', 'w') 
with open('dldb.json', 'r') as handle:
    parsed=json.load(handle)
output.write(json.dumps(parsed, indent=4, sort_keys=True))
output.close()


