import GAthon

# Please identify your project before doing any queries
# This only has to be done once at the beginning
# Feel free to use the repo's github link for Contact Email
GAthon.set_client("<Project Name>", "<Project Version>", "<Contact Email>")

# Example Showcase for GAQuery
# Create the GAQuery class
# There are too many variables, create a GAQuery class, then set your search parameters.
# You can stack multiple search paramaters in a single GAQuery class
queryInfo = GAthon.GAQuery()

# Search via name
# Calling add_name again will overwrite the previous name that was set
queryInfo.add_name("Kong Ming")

# Search via sets
# You can add multiple sets by calling add_set again
queryInfo.add_set("AMB")

# Accessing Multiface Cards
queryInfo = GAthon.GAQuery()
queryInfo.add_name("Lu Bu")
data = GAthon.Search(query=queryInfo)[0]
print(data.editions[0].other_orientations[0].editions[0].set_info.name)