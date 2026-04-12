# Helper Libraries
import GAthon.GAEnums as GAEnums
import json
import GACardData

# # Python Libraries
import httpx
from urllib.parse import quote_plus
from dataclasses import dataclass
from typing import Optional

# --- HTTPX --- #
client: Optional[httpx.Client] = None

# --- API Params --- #
api_link = "https://api.gatcg.com"
query_link = api_link + "/cards/search?"

def set_client(app_name: str, ver: str, contact: str = None):
    global client
    user_agent = f"{app_name}/{ver}"
    if (contact is not None):
        user_agent += f"{contact}"
    client = httpx.Client(headers={"User-Agent": user_agent})

@dataclass
class GAQuery:
    # Name
    __name: Optional[str] = None
    def add_name(self, name: str) -> "GAQuery":
        self.__name = name
        return self
    def clear_name(self) -> "GAQuery":
        self.__name = None
    @property
    def name(self) -> Optional[str]:
        return self.__name

    # Sets
    __sets: Optional[list[str]] = None
    def add_set(self, set_name: str) -> "GAQuery":
        if (self.__sets is None):
            self.__sets = []
        self.__sets.append(set_name)
        return self
    def clear_set(self) -> "GAQuery":
        self.__sets = None
        return self
    @property
    def sets(self) -> Optional[list[str]]:
        return self.__sets

    # Elements 
    __elements: Optional[list[GAEnums.Elements]] = None
    def add_element(self, element: GAEnums.Elements) -> "GAQuery":
        if (self.__elements is None):
            self.__elements = []
        self.__elements.append(element)
        return self
    def clear_elements(self) -> "GAQuery":
        self.__elements = None
        return self
    __all_elements = False
    def all_elements(self, val: bool) -> "GAQuery":
        self.__all_elements = val
        return self
    @property
    def elements(self) -> Optional[list[GAEnums.Elements]]:
        return self.__elements
    @property
    def all_element(self) -> Optional[bool]:
        return self.__all_elements

    # Classes
    __classes: Optional[list[GAEnums.Classes]] = None
    def add_class(self, ga_class: GAEnums.Classes) -> "GAQuery":
        if (self.__classes is None):
            self.__classes = []
        self.__classes.append(ga_class)
        return self
    def clear_classes(self) -> "GAQuery":
        self.__classes = None
        return self
    __all_classes = False
    def all_classes(self, val:bool) -> "GAQuery":
        self.__all_classes = val
        return self
    @property
    def classes(self) -> Optional[list[GAEnums.Classes]]:
        return self.__classes
    @property
    def all_class(self) -> Optional[bool]:
        return self.__all_classes
    
    # Card Types
    __types: Optional[list[GAEnums.Types]] = None
    def add_type(self, ga_type: GAEnums.Types) -> "GAQuery":
        if (self.__types is None):
            self.__types = []
        self.__types.append(ga_type)
        return self
    def clear_types(self) -> "GAQuery":
        self.__types = None
        return self
    __all_types = False
    def all_types(self, val:bool) -> "GAQuery":
        self.__all_types = val
        return self
    @property
    def types(self) -> Optional[list[GAEnums.Types]]:
        return self.__types
    @property
    def all_type(self) -> Optional[bool]:
        return self.__all_types
    
    # Effects
    __effect: Optional[str] = None
    def add_effect(self, effect: str) -> "GAQuery":
        self.__effect = effect
        return self
    def clear_effect(self) -> "GAQuery":
        self.__effect = None
        return self
    @property
    def effect(self) -> Optional[str]:
        return self.__effect

    # Rarities
    __rarities: Optional[list[GAEnums.Rarity]] = None
    def add_rarity(self, ga_rarity: GAEnums.Rarity) -> "GAQuery":
        if (self.__rarities is None):
            self.__rarities = []
        self.__rarities.append(ga_rarity)
        return self
    def clear_rarities(self) -> "GAQuery":
        self.__rarities = None
        return self
    @property
    def rarities(self) -> Optional[list[GAEnums.Rarity]]:
        return self.__rarities
    
    # Card Subtypes
    __subtypes: Optional[list[GAEnums.Subtypes]] = None
    def add_subtype(self, ga_subtype: GAEnums.Subtypes) -> "GAQuery":      # Fix #2
        if (self.__subtypes is None):
            self.__subtypes = []
        self.__subtypes.append(ga_subtype)
        return self
    def clear_subtypes(self) -> "GAQuery":
        self.__subtypes = None
        return self
    __all_subtypes = False
    def all_subtypes(self, val:bool) -> "GAQuery":
        self.__all_subtypes = val
        return self
    @property
    def subtypes(self) -> Optional[list[GAEnums.Subtypes]]:
        return self.__subtypes
    @property
    def all_subtype(self) -> Optional[bool]:
        return self.__all_subtypes
    
    # Logical Operations
    __operations: Optional[list[tuple[GAEnums.LogicParameter, GAEnums.LogicOperator, int]]] = None
    def add_operation(self, param: GAEnums.LogicParameter, operator: GAEnums.LogicOperator, val:int) -> "GAQuery":
        if (self.__operations is None):
            self.__operations = []
        self.__operations.append((param, operator, str(val)))
        return self
    def clear_operations(self) -> "GAQuery":
        self.__operations = None
        return self
    @property
    def operations(self) -> Optional[list[str]]:
        return self.__operations
    
    # Speed
    __speeds: Optional[list[str]] = None
    def add_speed(self, speed: GAEnums.Speed) -> "GAQuery":
        if (self.__speeds is None):
            self.__speeds = []
        if (len(self.__speeds) == 2):
            return self
        self.__speeds.append(speed)
        return self
    def clear_speeds(self) -> "GAQuery":
        self.__speeds = None
        return self
    @property
    def speeds(self) -> Optional[list[str]]:
        return self.__speeds
    
    # Configuration
    __configuration: Optional[list[str]] = None
    def add_configuration(self, config: GAEnums.Configuration) -> "GAQuery":
        if (self.__configuration is None):
            self.__configuration = []
        self.__configuration.append(config)
        return self
    def clear_configurations(self) -> "GAQuery":
        self.__configuration = None
        return self
    @property
    def configuration(self) -> Optional[list[str]]:
        return self.__configuration
    
    # Collector Number
    __collector_number: Optional[str] = None
    def add_collector_number(self, num: str) -> "GAQuery":
        self.__collector_number = num
        return self
    def clear_collector_number(self) -> "GAQuery":
        self.__collector_number = None
        return self
    @property
    def collector_number(self) -> Optional[int]:
        return self.__collector_number
    
    # Illustrator
    __illustrator: Optional[str] = None
    def add_illustrator(self, name: str) -> "GAQuery":
        self.__illustrator = name
        return self
    def clear_illustrator(self) -> "GAQuery":
        self.__illustrator = None
        return self
    @property
    def illustrator(self) -> Optional[str]:
        return self.__illustrator
    
    # Languages
    __languages: Optional[list[GAEnums.Language]] = None
    def add_language(self, lang: GAEnums.Language) -> "GAQuery":
        if (self.__languages is None):
            self.__languages = []
        self.__languages.append(lang)
        return self
    def clear_languages(self) -> "GAQuery":
        self.__languages = None
        return self
    @property
    def languages(self) -> Optional[list[GAEnums.Language]]:
        return self.__languages
    
    # Flavor
    __flavor: Optional[str] = None
    def add_flavor(self, text: str) -> "GAQuery":
        self.__flavor = text
        return self
    def clear_flavor(self) -> "GAQuery":
        self.__flavor = None
        return self
    @property
    def flavor(self) -> Optional[str]:
        return self.__flavor
    
    # Slug
    __slug: Optional[str] = None
    def add_slug(self, text:str) -> "GAQuery":
        self.__slug = text
        return self
    def clear_slug(self) -> "GAQuery":
        self.__slug = None
        return self
    @property
    def slug(self) -> Optional[str]:
        return self.__slug

    # Legality
    __legality: Optional[tuple[GAEnums.Format, GAEnums.Legality]] = None
    def add_legality(self, format: GAEnums.Format, legality: GAEnums.Legality) -> "GAQuery":
        self.__legality = (format, legality)
        return self
    def clear_legality(self) -> "GAQuery":
        self.__legality = None
        return self
    @property
    def legality(self) -> Optional[tuple[GAEnums.Format, GAEnums.Legality]]:
        return self.__legality
    
    # Edition Effect
    __edition_effect: Optional[str] = None
    def add_edition_effect(self, effect: str) -> "GAQuery":
        self.__edition_effect = effect
        return self
    def clear_edition_effect(self) -> "GAQuery":
        self.__edition_effect = None
        return self
    @property
    def edition_effect(self) -> Optional[str]:
        return self.__edition_effect
    
    # Edition Flavor
    __edition_flavor: Optional[str] = None
    def add_edition_flavor(self, flavor: str) -> "GAQuery":
        self.__edition_flavor = flavor
        return self
    def clear_edition_flavor(self) -> "GAQuery":
        self.__edition_flavor = None
        return self
    @property
    def edition_flavor(self) -> Optional[str]:
        return self.__edition_flavor

    # Edition Slug
    __edition_slug: Optional[str] = None
    def add_edition_slug(self, text: str) -> "GAQuery":
        self.__edition_slug = text
        return self
    def clear_edition_slug(self) -> "GAQuery":
        self.__edition_slug = None
        return self
    @property
    def edition_slug(self) -> Optional[str]:
        return self.__edition_slug

    # Collab
    __collab: Optional[bool] = None
    def add_collab(self, val: bool) -> "GAQuery":
        self.__collab = val
        return self
    @property
    def collab(self) -> Optional[bool]:
        return self.__collab
    
    # Separate Editions
    __separate_editions: Optional[bool] = None
    def add_seperate_editions(self, val: bool) -> "GAQuery":
        self.__separate_editions = val
        return self
    @property
    def separate_editions(self) -> Optional[bool]:
        return self.__separate_editions
    
    def __str__(self):
        printVal = ""

        # Name
        if (self.__name is not None):
            printVal += ("Name: " + self.__name + "\n")
        # Sets
        if (self.__sets is not None):
            printVal += ("Sets: ")
            for setName in self.__sets:
                printVal += (setName + " ")
            printVal += "\n"
        # Elements
        if (self.__elements is not None):
            printVal += ("Elements: ")
            for elem in self.__elements:
                printVal += (elem.value + " ")
            printVal += "\n"
        # Classes
        if (self.__classes is not None):
            printVal += ("Classes: ")
            for gaClass in self.__classes:
                printVal += (gaClass.value + " ")
            printVal += "\n"
        # Types
        if (self.__types is not None):
            printVal += ("Types: ")
            for gaType in self.__types:
                printVal += (gaType.value + " ")
            printVal += "\n"
        # Effect
        if (self.__effect is not None):
            printVal += ("Effect: " + self.__effect + "\n")
        # Rarities
        if (self.__rarities is not None):
            printVal += ("Rarities: ")
            for rarity in self.__rarities:
                printVal += (rarity.value + " ")
            printVal += "\n"
        # Subtypes
        if (self.__subtypes is not None):
            printVal += ("Subtypes: ")
            for subtype in self.__subtypes:
                printVal += (subtype.value + " ")
            printVal += "\n"
        # Logical Operations
        if (self.__operations is not None):
            for operation in self.__operations:
                printVal += ("Operation: " + operation[0].name + " " + operation[1].name + " " + operation[2] + "\n")
        # Speeds
        if (self.__speeds is not None):
            printVal += ("Speeds: ")
            for speed in self.__speeds:
                printVal += (speed.value + " ")
            printVal += "\n"
        # Configuration
        if (self.__configuration is not None):
            printVal += ("Configuration: ")
            for config in self.__configuration:
                printVal += (config.value + " ")
            printVal += "\n"
        # Collector Number
        if (self.__collector_number is not None):
            printVal += ("Collector Number: " + str(self.__collector_number) + "\n")
        # Illustrator
        if (self.__illustrator is not None):
            printVal += ("Illustrator: " + self.__illustrator + "\n")
        # Languages
        if (self.__languages is not None):
            printVal += ("Languages: ")
            for lang in self.__languages:
                printVal += (lang.value + " ")
            printVal += "\n"
        # Flavor
        if (self.__flavor is not None):
            printVal += ("Flavor: " + self.__flavor + "\n")
        # Slug
        if (self.__slug is not None):
            printVal += ("Slug: " + self.__slug + "\n")
        # Legality
        if (self.__legality is not None):
            printVal += ("Legality: " + self.__legality[0].name + " " + self.__legality[1].name + "\n")
        # Edition Effect
        if (self.__edition_effect is not None):
            printVal += ("Edition Effect: " + self.__edition_effect + "\n")
        # Edition Slug
        if (self.__edition_slug is not None):
            printVal += ("Edition Slug: " + self.__edition_slug + "\n")
        # Collab
        if (self.__collab is not None):
            printVal += ("Collab: " + str(self.__collab) + "\n")
        # Separate Editions
        if (self.__separate_editions is not None):
            printVal += ("Separate Editions: " + str(self.__separate_editions) + "\n")

        return printVal
    
def Search(query: GAQuery) -> list[GACardData.GACardData]:

    if (client is None):
        return

    query_params = []

    #-----------------------------#
    # --- Start Parsing Query --- #
    #-----------------------------#

    # Name
    if (query.name is not None):
        query_params.append(f"name={quote_plus(query.name)}")

    # Sets
    if (query.sets is not None):
        for setInfo in query.sets:
            query_params.append(f"prefix={setInfo}")

    # Elements
    if (query.elements is not None):
        for element in query.elements:
            query_params.append(f"element={element.value}")
    if (query.all_element is True):
        query_params.append(f"element_logic=AND")

    # Classes
    if (query.classes is not None):
        for gaclass in query.classes:
            query_params.append(f"class={gaclass.value}")
    if (query.all_class is True):
        query_params.append("class_logic=AND")

    # Types
    if (query.all_type is True):
        query_params.append("type_logic=AND")
    if (query.types is not None):
        for gatype in query.types:
            query_params.append(f"type={gatype.value}")

    # Effect
    if (query.effect is not None):
        query_params.append(f"effect={query.effect}")

    # Rarities
    if (query.rarities is not None):
        for rarity in query.rarities:
            query_params.append(f"rarity={rarity.value}")

    # Subtypes
    if (query.all_subtype is True):
        query_params.append("subtype_logic=AND")
    if (query.subtypes is not None):
        for subtype in query.subtypes:
            query_params.append(f"subtype={subtype.value}")

    # Logical Operators
    if (query.operations is not None):
        operations_str = ""
        for i in range(len(query.operations)):
            operations_str += query.operations[i][0].value + query.operations[i][1].value + str(query.operations[i][2])
            if (i is not (len(query.operations) - 1)):
                operations_str += ";"
        query_params.append(f"stats={operations_str}")

    # Speed
    if (query.speeds is not None):
        for speed in query.speeds:
            query_params.append(f"speed={speed.value}")

    # Configuration
    if (query.configuration is not None):
        for config in query.configuration:
            query_params.append(f"configuration={config.value}")

    # Collector Number
    if (query.collector_number is not None):
        query_params.append(f"collector_number={query.collector_number}")

    # Illustrator
    if (query.illustrator is not None):
        query_params.append(f"illustrator={query.illustrator}")

    # Language
    if (query.languages is not None):
        for language in query.languages:
            query_params.append(f"language={language.value}")

    # Flavor
    if (query.flavor is not None):
        query_params.append(f"flavor={query.flavor}")

    # Slug
    if (query.slug is not None):
        query_params.append(f"slug={query.slug}")

    # Legality
    if (query.legality is not None):
        query_params.append(f"legality_format={query.legality[0].value}")
        query_params.append(f"legality_state={query.legality[1].value}")

    # Edition Effect
    if (query.edition_effect is not None):
        query_params.append(f"edition_effect={query.edition_effect}")

    # Edition Flavor
    if (query.edition_flavor is not None):
        query_params.append(f"edition_flavor={query.edition_flavor}")

    # Edition Slug
    if (query.edition_slug is not None):
        query_params.append(f"edition_slug={query.edition_slug}")

    # Collaborations
    if (query.collab is True):
        query_params.append(f"collab=true")

    # Seperate Editions
    if (query.separate_editions is True):
        query_params.append(f"separate_editions=true")

    #-----------------------------#
    # ---  End Parsing Query  --- #
    #-----------------------------#

    param_list = "&".join(query_params)

    response = client.get(query_link, params=param_list)
    print(f"Fetching data from {response.url}")
    if (response.status_code == 200):
        data = response.json()
        returnData = []
        cardDataList = data.get("data")
        for cardData in cardDataList:
            returnData.append(GACardData.GACardData(cardData))
        return returnData
    else:
        print("Error fetching response!")
        return None
    
def QuickSearch(name: str) -> list[GACardData.GACardData]:
    gaQuery = GAQuery()
    gaQuery.add_name(name)
    return Search(gaQuery)