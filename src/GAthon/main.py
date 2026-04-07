import requests
import GAQuery
import enums

query = GAQuery.GAQuery()
query.add_operation(enums.LogicParameter.NONFOIL_THEMA_MYSTI, enums.LogicOperator.GREATER_THAN, 4)
query.add_legality(enums.Format.PANTHEON, enums.Legality.LEGAL)

print(query)


# response = requests.get("https://api.gatcg.com/cards/search?name=kongming&element=TERA")
# if response.status_code == 200:
#     # 3. Parse JSON data
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")