import GAthon

#--------------------------------------------------#
#              Querying Example                    # 
#--------------------------------------------------#

# Please identify your project before doing any queries
# This only has to be done once at the beginning
# Feel free to use the repo's github link for Contact Email
GAthon.set_client("<Project Name>", "<Project Version>", "<Contact Email>")

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
queryInfo.add_set("DOA")

# Search via Elements
# You can add multiple elements by calling add_element again
# Note that Exalted is an element on the GA Index query
# All elements available are indexed under GAthon.Elements
queryInfo.add_element(GAthon.Elements.WATER)
queryInfo.add_element(GAthon.Elements.EXALTED)

# Search via Classes
# You can add multiple classes by calling add_class again
# Default search is "Any" of the listed classes
# This can be changed to search for "All" listed classes by calling all_classes with True
# All classes available are indexed under GAthon.Classes
queryInfo.add_class(GAthon.Classes.MAGE)
queryInfo.add_class(GAthon.Classes.ANOMALY)
queryInfo.all_classes(True)

# Search via Types
# You can add multiple types by calling add_type again
# Default search is "Any" of the listed types
# This can be changed to search for "All" listed types by calling all_types with True
# All types available are indexed under GAthon.Types
queryInfo.add_type(GAthon.Types.CHAMPION)
queryInfo.add_type(GAthon.Types.UNIQUE)
queryInfo.all_types(True)

# Search via Effect
# Calling add_effect again will overwrite the previous effect that was set
# Quoting from the GA Index Website:
# "Black bubbles like Class bonus should be wrapped in square brackets (e.g. "[Class bonus]")"
# "Yellow bubbles like 2 should be wrapped in regular brackets (e.g. "pay (2)")"
# "Icons like ♡, ⚔︎ and ⤵ should use their regular names ("life", "power" and "rest" respectively)"
queryInfo.add_effect("Floating Memory")

# Search via Rarity
# You can add multiple rarities by calling add_rarity again
# All typess available are indexed under GAthon.Rarity
queryInfo.add_rarity(GAthon.Rarity.COMMON)
queryInfo.add_rarity(GAthon.Rarity.C_SUPER_RARE)

# Search via Subtypes
# You can add multiple subtypes by calling add_subtype again
# Default search is "Any" of the listed subtypes
# This can be changed to search for "All" listed subtypes by calling all_subtypes with True
# All subtypes available are indexed under GAthon.subtypes
queryInfo.add_subtype(GAthon.Subtypes.BOOK)
queryInfo.add_subtype(GAthon.Subtypes.HUMAN)
queryInfo.all_subtypes(True)

# Search via Logic Operators
# You can add multiple operators by calling add_operator again
# All logic parameters and operators are indexed under GAthon.LogicParameter and GAthon.LogicOperator respectively
queryInfo.add_operation(GAthon.LogicParameter.MEMORY_COST, GAthon.LogicOperator.EQUAL_TO, 1) # Memory Cost = 1
# Since the value passed in must be an int, to search by rarity you may use the Rarity enum, and use the value which is an int
queryInfo.add_operation(GAthon.LogicParameter.RARITY, GAthon.LogicOperator.GREATER_THAN, GAthon.Rarity.COMMON.value) # Rarity > Common

# Search via Speed
# You can add multiple speeds by calling add_speed again
# All logic parameters and operators are indexed under GAthon.Speed
queryInfo.add_speed(GAthon.Speed.NONE)
queryInfo.add_speed(GAthon.Speed.FAST)

# Search via Configuration
# You can add multiple configurations by calling add_configuration again
# {Although, there is only 2 configuration for cards as of writing this}
# All logic parameters and operators are indexed under GAthon.Configuration
queryInfo.add_configuration(GAthon.Configuration.DEFAULT)
queryInfo.add_configuration(GAthon.Configuration.FLIP)

# Search via Collecter Number
# Calling add_collector_number again will overwrite the previous collector number
# Note that this is a string, "007" vs "7" are parsed differently by GA Index
queryInfo.add_collector_number("007")

# Search via Illustrator
# Calling add_illustrator again will overwrite the previous illustrator
queryInfo.add_illustrator("十尾")

# Search via Language
# You can add multiple languages by calling add_language again
# All logic parameters and operators are indexed under GAthon.Language
queryInfo.add_language(GAthon.Language.CHINESE)
queryInfo.add_language(GAthon.Language.ENGLISH)

# Search via Flavor text
# Calling add_flavor again will overwrite the previous flavor text
queryInfo.add_flavor("A lily pad is but a weed in a pond of lotuses.")

# Search via card slug
# Calling add_slug again will overwrite the previous slug
queryInfo.add_slug("kongming-wayward-maven")

# Search via card legality
# Calling add_legality again will overwrite the previous legality settings
# All formats and legalities are indexed under GAthon.Format and GAthon.Legality respectively
queryInfo.add_legality(GAthon.Format.PANTHEON, GAthon.Legality.LEGAL)

# Search via Edition Effect
# Calling add_edition_effect again will overwrite the previous edition effect
# Quoting from the GA Index Website:
# "This is less precise than using the above Effect field which searches on both card and edition effects."
# "Most editions inherit their effect from the card, which will not be matched by this field."
queryInfo.add_edition_effect("Floating Memory")

# Search via Edition Flavor
# Calling add_edition_flavor again will overwrite the previous edition flavor
# Quoting from the GA Index Website:
# "This is less precise than using the above Flavor field which searches on both card and edition flavors."
queryInfo.add_edition_flavor("A lily pad is but a weed in a pond of lotuses.")

# Search via Edition Slug
# Calling add_edition_slug again will overwrite the previous edition slug
# This will return a single card edition if a match is found
queryInfo.add_edition_slug("kongming-wayward-maven-amb")

# Enable/Disable collaborations tag
queryInfo.add_collab(True)

# Enable/Disable seperate editions
# This will cause each card data to be its own edition, instead of being grouped
queryInfo.add_seperate_editions(True)

# Then to query, use the GAthon.Search function, and pass in the Query class as the argument
# The result data will be returned as a list of GACardData
# For more information about the data structure, view DataExamples.py
result = GAthon.Search(queryInfo)

# To perform a search via name without making any classes, use QuickSearch
result = GAthon.QuickSearch("Kong Ming, Wayward Maven")