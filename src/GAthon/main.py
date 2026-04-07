import GAQuery
import enums

GAQuery.set_client("GAthon", "0.0.1", "tankangzheng@hotmail.com")

queryInfo = GAQuery.GAQuery()
queryInfo.add_element(enums.Elements.TERA)
queryInfo.add_class(enums.Classes.MAGE)
queryInfo.add_operation(enums.LogicParameter.RESERVE_COST, enums.LogicOperator.GREATER_THAN, 3)
queryInfo.add_speed(enums.Speed.FAST)
queryInfo.add_speed(enums.Speed.SLOW)

GAQuery.Search(query=queryInfo)

# response = requests.get("https://api.gatcg.com/cards/search?name=kongming&element=TERA")
# if response.status_code == 200:
#     # 3. Parse JSON data
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")