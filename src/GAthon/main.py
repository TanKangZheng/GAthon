import GAQuery
import enums

GAQuery.set_client("GAthon", "0.0.1", "tankangzheng@hotmail.com")

queryInfo = GAQuery.GAQuery()
queryInfo.add_type(enums.Types.ACTION)
queryInfo.add_type(enums.Types.ATTACK)

GAQuery.Search(query=queryInfo)

# response = requests.get("https://api.gatcg.com/cards/search?name=kongming&element=TERA")
# if response.status_code == 200:
#     # 3. Parse JSON data
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")