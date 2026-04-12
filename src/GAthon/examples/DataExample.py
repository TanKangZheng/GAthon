import GAthon

#--------------------------------------------------#
#              CardData Example                    # 
#--------------------------------------------------#
queryInfo = GAthon.GAQuery()
queryInfo.add_slug("kongming-wayward-maven")
CardData = GAthon.Search(queryInfo)[0]

# If a data returns None, it is likely that the result json was empty as well

# Classes
# A list of strings of the card's class(es)
print(CardData.classes)

# Memory Cost
# The value of the card's memory cost. Will be None if cost type is reserve
# This is a deprecated data entry
print(CardData.cost_memory)

# Reserve Cost
# The value of the card's reserve cost. Will be None if cost type is Memory
# This is a deprecated data entry
print(CardData.cost_reserve)

# Cost
# A tuple of [str, int]. str being the cost type, and int being the value
print(CardData.cost)

# Created At
# A string containins the timestamp that this data was created on the GA Index website
print(CardData.created_at)

# Editions
# A list of GACardEdition, each being the data for each edition of the card printed
# For this example, the code below will print out the set name for each edition
for editionData in CardData.editions:
    print(editionData.set_info.name)

# Effect
# A string containing the formatted effect text
print(CardData.effect)

# Effect (Raw)
# A string containing the effect text, without any text formatting
print(CardData.effect_raw)

# Element
# A string containing the element of the card
# This is a deprecated data entry
print(CardData.element)

# Elements
# A list of strings of the elements of the card
for elementData in CardData.elements:
    print(elementData)

# Flavor
# A string containing the flavor text of the card
print(CardData.flavor)

# Legality
# A list of tuples [str, int] containing the limits of the card in a restricted format
for legalityData in CardData.legality:
    print(f"Format: {legalityData[0]}, Limit: {legalityData[1]}")

# Level
# The level of the card as an int
print(CardData.level)

# Life
# The list total of the card as an int
print(CardData.life)

# Name
# The name of the card as a string
print(CardData.name)

# Power
# The power of the card as an int
print(CardData.power)

# References
# A list of Reference, each being the data for a referenced card
# # The code segment prints the name of each referenced card
for referenceData in CardData.references:
    print(referenceData.name)

# Result Editions
# A list of GACardEdition, each being the data for each edition of the card printed
# For this example, the code below will print out the set name for each edition
for resultEditionData in CardData.result_editions:
    print(resultEditionData.set_info.name)

# Rules
# A list of rules that are present on the card
for rulesData in CardData.rules:
    print(rulesData)

# Slug
# The slug for the card as a string
print(CardData.slug)

# Speed
# The speed of the card as a string
print(CardData.speed)

# Subtypes
# A list of subtypes of the card
for subtypeData in CardData.subtypes:
    print(subtypeData)

# Types
# A list of types of the card
for typeData in CardData.types:
    print(typeData)

# UUID
# The UUID of the card
print(CardData.uuid)

# Effect HTML
# A string containing the effect text of the card, formatted for HTML
print(CardData.effect_html)

#--------------------------------------------------#
#            CardEdition Example                   # 
#--------------------------------------------------#
CardEdition = CardData.editions[0]

# Card ID
# The edition's card ID as a string
print(CardEdition.card_id)

# Collector number
# The Collector Number for this edition of the card
print(CardEdition.collector_number)

# Configuration
# The configuration of the card (Default, Flip etc)
print(CardEdition.configuration)

# Created At
# The timestamp of when this edition data was created on the GA Index Website
print(CardEdition.created_at)

# Effect
# A string containing the formatted effect text for this edition
print(CardEdition.effect)

# Effect (Raw)
# A string containing the effect text for this edition, without any text formatting
print(CardEdition.effect_raw)

# Flavor
# A string containing the falvor text of the card edition
print(CardEdition.flavor)

# Illustrator
# The illustrator for this card edition's image
print(CardEdition.illustrator)

# Img Link
# The link to the image of this card edition
print(CardEdition.img_link)

# Orientation
# The orientation of this card edition
print(CardEdition.orientation)

# Rarity
# The rarity of the card, as an int
# Since the value returned is an int, to convert by rarity you can use GAEnums.Elements
print(GAthon.GAEnums(CardEdition.rarity))

# Slug
# The slug for this card edition
print(CardEdition.slug)

# Thema
# The multitude of thema scores for this card edition
# Theres too many of them so I will list them all here
print(f"Thema Foil: {CardEdition.thema_foil}")
print(f"Thema Nonfoil: {CardEdition.thema_nonfoil}")

print(f"Thema Charm Foil: {CardEdition.thema_charm_foil}")
print(f"Thema Charm Nonfoil: {CardEdition.thema_charm_nonfoil}")

print(f"Thema Ferocity Foil: {CardEdition.thema_ferocity_foil}")
print(f"Thema Ferocity Nonfoil: {CardEdition.thema_ferocity_nonfoil}")

print(f"Thema Grace Foil: {CardEdition.thema_grace_foil}")
print(f"Thema Grace Nonfoil: {CardEdition.thema_grace_nonfoil}")

print(f"Thema Mystique Foil: {CardEdition.thema_mystique_foil}")
print(f"Thema Mystique Nonfoil: {CardEdition.thema_mystique_nonfoil}")

print(f"Thema Valor Foil: {CardEdition.thema_valor_foil}")
print(f"Thema Valor Nonfoil: {CardEdition.thema_valor_nonfoil}")

print(f"Thema Foil Dynamic: {CardEdition.thema_foil_dynamic}")
print(f"Thema Nonfoil Dynamic: {CardEdition.thema_nonfoil_dynamic}")

# UUID
# The UUID of this card edition
print(CardEdition.uuid)

# Collaborators
# A list of collaborators that are credited to this card edition
for collaboratorData in CardEdition.collaborators:
    print(collaboratorData)

# Circulation Template
# A List of CirculationTemplate for this card edition
# This code segment prints the name for each Circulation Template
for circulationTemplateData in CardEdition.circulation_template:
    print(circulationTemplateData.name)

# Circulations
# A List of CirculationTemplate for this card edition
# This code segment prints the name for each Circulation
for circulationData in CardEdition.circulations:
    print(circulationData.name)

# Other Orientations
# A list of CardData of other orientations of this card edition
# This code segment prints the name for each other orientation
for otherOrientationData in CardEdition.other_orientations:
    print(otherOrientationData.name)

# Set Info
# The set info for this card edition
# This code segment prints the name for the set edition
print(CardEdition.set_info.name)

# Effect HTML
# A string containing the effect text of the card, formatted for HTML
print(CardEdition.effect_html)