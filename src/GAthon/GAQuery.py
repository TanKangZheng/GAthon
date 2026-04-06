import enums
from dataclasses import dataclass, field
from typing import Optional

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
    __elements: Optional[list[enums.Elements]] = None
    def add_element(self, element: enums.Elements) -> "GAQuery":
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
    def elements(self) -> Optional[list[enums.Elements]]:
        return self.__elements

    # Classes
    __classes: Optional[list[enums.Classes]] = None
    def add_class(self, ga_class: enums.Classes) -> "GAQuery":
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
    def classes(self) -> Optional[list[enums.Classes]]:
        return self.__classes
    
    # Card Types
    __types: Optional[list[enums.Types]] = None
    def add_type(self, ga_type: enums.Types) -> "GAQuery":
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
    def types(self) -> Optional[list[enums.Types]]:
        return self.__types
    
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
    __rarities: Optional[list[enums.Rarity]] = None
    def add_rarity(self, ga_rarity: enums.Rarity) -> "GAQuery":
        if (self.__rarities is None):
            self.__rarities = []
        self.__rarities.append(ga_rarity)
        return self
    def clear_rarities(self) -> "GAQuery":
        self.__rarities = None
        return self
    @property
    def rarities(self) -> Optional[list[enums.Rarity]]:
        return self.__rarities
    
    # Card Subtypes
    __subtypes: Optional[list[enums.Subtypes]] = None
    def add_subtype(self, ga_subtype: enums.Subtypes) -> "GAQuery":      # Fix #2
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
    def subtypes(self) -> Optional[list[enums.Subtypes]]:
        return self.__subtypes
    
    # Logical Operations
    __operations: Optional[list[str]] = None
    def add_operation(self, param: enums.LogicParameter, operator: enums.LogicOperator, val:int) -> "GAQuery":
        if (self.__operations is None):
            self.__operations = []
        self.__operations.append((param.value, operator.value, str(val)))
        return self
    def clear_operations(self) -> "GAQuery":
        self.__operations = None
        return self
    @property
    def operations(self) -> Optional[list[str]]:
        return self.__operations
    
    # Speed
    __speeds: Optional[list[str]] = None
    def add_speed(self, speed: enums.Speed) -> "GAQuery":
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
    def add_configuration(self, config: enums.Configuration) -> "GAQuery":
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
    __collector_number: Optional[int] = None
    def add_collector_number(self, num: int) -> "GAQuery":
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
    __languages: Optional[list[enums.Language]] = None
    def add_language(self, lang: enums.Language) -> "GAQuery":
        if (self.__languages is None):
            self.__languages = []
        self.__languages.append(lang)
        return self
    def clear_languages(self) -> "GAQuery":
        self.__languages = None
        return self
    @property
    def languages(self) -> Optional[list[enums.Language]]:
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
    __legality: Optional[tuple[enums.Format, enums.Legality]] = None
    def add_legality(self, format: enums.Format, legality: enums.Legality) -> "GAQuery":
        self.__legality = (format, legality)
        return self
    def clear_legality(self) -> "GAQuery":
        self.__legality = None
        return self
    @property
    def legality(self) -> Optional[tuple[enums.Format, enums.Legality]]:
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
                printVal += (elem + " ")
            printVal += "\n"
        # Classes
        if (self.__classes is not None):
            printVal += ("Classes: ")
            for gaClass in self.__classes:
                printVal += (gaClass + " ")
            printVal += "\n"
        # Types
        if (self.__types is not None):
            printVal += ("Types: ")
            for gaTypes in self._types:
                printVal += (gaTypes + " ")
            printVal += "\n"
        # Effect
        if (self.__effect is not None):
            printVal += ("Effect: " + self.__effect + "\n")

        return printVal