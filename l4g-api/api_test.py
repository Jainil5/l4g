import requests
import json

BASE = "http://127.0.0.1:5000/query/"

x= "In accounts generate a q generate a query for names where billing city is surat, bipoc head is Modi and active program cohort is 0"
res = requests.get(BASE + x)
#response = requests.post(BASE+"helloworld")
print(res.json())
