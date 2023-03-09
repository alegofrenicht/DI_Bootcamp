# 🌟 Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
 }"""

#
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
jsonstring = json.loads(sampleJson)
print(f"'salary' key: {jsonstring['company']['employee']['payable']['salary']}")
jsonstring['company']['employee']['birth_date'] = '1999/09/04'
with open('sample.json', 'w') as sjs:
    json.dump(jsonstring, sjs, indent=2, sort_keys=True)
