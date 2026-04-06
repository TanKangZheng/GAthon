import requests
import GAQuery
import enums

query = GAQuery.GAQuery()
query.add_name("Test")
query.add_set("RDO").add_set("RDOP")
query.add_element(enums.Elements.ASTRA)

print(query)


# response = requests.get("https://api.gatcg.com/cards/search?name=kongming&element=TERA")
# if response.status_code == 200:
#     # 3. Parse JSON data
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")