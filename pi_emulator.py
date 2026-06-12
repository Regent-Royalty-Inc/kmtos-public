import requests, json

target = "http://10.0.0.113:7070/ra-reveal"
payload = {"text": "ra reveal example"}

r = requests.post(target, json=payload)
print(json.dumps(r.json(), indent=2))

