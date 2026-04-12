import GAthon.GAEnums as GAEnums
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class CirculationTemplate:
    #Created At
    created_at: Optional[str] = None

    # Edition ID
    edition_id: Optional[str] = None

    # Foil
    foil: Optional[bool] = None

    # Kind
    kind: Optional[str] = None

    # Name
    name: Optional[str] = None

    # Population
    population: Optional[int] = None

    # Population Operator
    population_operator: Optional[str] = None

    # Printing
    printing: Optional[bool] = None

    # UUID
    uuid: Optional[str] = None

    # Init
    def __init__(self, data: dict):
        # Created At
        self.created_at = data.get("created_at")
        # Edition ID
        self.edition_id = data.get("edition_id")
        # Foil
        self.foil = data.get("foil")
        # Kind
        self.kind = data.get("kind")
        # Population
        self.population = data.get("population")
        # Population Operator
        self.population_operator = data.get("population_operator")
        # Printing
        self.printing = data.get("printing")
        # UUID
        self.uuid = data.get("uuid")

    def __str__(self) -> str:
        result = ""

        # Name
        if self.name is not None:
            result += f"Name: {self.name}\n"
        # UUID
        if self.uuid is not None:
            result += f"UUID: {self.uuid}\n"
        # Edition ID
        if self.edition_id is not None:
            result += f"Edition ID: {self.edition_id}\n"
        # Kind
        if self.kind is not None:
            result += f"Kind: {self.kind}\n"
        # Population
        if self.population is not None:
            result += f"Population: {self.population}\n"
        # Population Operator
        if self.population_operator is not None:
            result += f"Population Operator: {self.population_operator}\n"
        # Foil
        if self.foil is not None:
            result += f"Foil: {self.foil}\n"
        # Printing
        if self.printing is not None:
            result += f"Printing: {self.printing}\n"
        # Created At
        if self.created_at is not None:
            result += f"Created At: {self.created_at}\n"

        return result

@dataclass
class SetInfo:
    # Created At
    created_at: Optional[str] = None

    # ID
    id: Optional[str] = None

    # Language
    language: Optional[str] = None

    # Name
    name: Optional[str] = None

    # Prefix
    prefix: Optional[str] = None

    # Release Date
    release_date: Optional[str] = None

    # Init
    def __init__(self, data: dict):
        # Created at
        self.created_at = data.get("created_at")
        # ID
        self.id = data.get("id")
        # Language
        self.language = data.get("language")
        # Name
        self.name = data.get("name")
        # Prefix
        self.prefix = data.get("prefix")
        # Release Date
        self.release_date = data.get("release_date")

    def __str__(self) -> str:
        result = ""

        # Name
        if self.name is not None:
            result += f"Name: {self.name}\n"
        # ID
        if self.id is not None:
            result += f"ID: {self.id}\n"
        # Prefix
        if self.prefix is not None:
            result += f"Prefix: {self.prefix}\n"
        # Language
        if self.language is not None:
            result += f"Language: {self.language}\n"
        # Release Date
        if self.release_date is not None:
            result += f"Release Date: {self.release_date}\n"
        # Created At
        if self.created_at is not None:
            result += f"Created At: {self.created_at}\n"

        return result

@dataclass
class Reference:
    # Kind
    kind: Optional[str] = None

    # Name
    name: Optional[str] = None

    # Slug
    slug: Optional[str] = None

    # Direction
    direction: Optional[str] = None

    # Init
    def __init__(self, data: dict):
        # Kind
        self.kind = data.get("kind")
        # Name
        self.name = data.get("name")
        # Slug
        self.slug = data.get("slug")
        # Direction
        self.direction = data.get("direction")

    def __str__(self) -> str:
        result = ""

        # Name
        if self.name is not None:
            result += f"Name: {self.name}\n"
        # Slug
        if self.slug is not None:
            result += f"Slug: {self.slug}\n"
        # Kind
        if self.kind is not None:
            result += f"Kind: {self.kind}\n"
        # Direction
        if self.direction is not None:
            result += f"Direction: {self.direction}\n"

        return result

@dataclass
class GACardData:
    # Classes
    classes: Optional[list[str]] = None

    # Cost
    cost_memory: Optional[int] = None
    cost_reserve: Optional[int] = None
    cost: Optional[tuple[str, int]] = None #str = Cost Type, int = value

    # Durability
    durability: Optional[int] = None

    # Created At
    created_at: Optional[str] = None

    # Editions
    editions: Optional[list["GACardEdition"]] = field(default_factory=list)

    # Effect
    effect: Optional[str] = None

    # Effect Raw
    effect_raw: Optional[str] = None

    # Element
    element: Optional[str] = None

    # Elements
    elements: Optional[list[str]] = None

    # Flavor
    flavor: Optional[str] = None

    # Legality
    legality: Optional[list[tuple[str, int]]] = None #str = Format, int = limit

    # Level
    level: Optional[int] = None

    # Life
    life: Optional[int] = None

    # Name
    name: Optional[str] = None

    # Power
    power: Optional[int] = None

    # References
    references: Optional[list[Reference]] = None

    # Result Editions
    result_editions: Optional[list["GACardEdition"]] = field(default_factory=list)

    # Rules
    rules: Optional[list[str]] = None

    # Slug
    slug: Optional[str] = None

    # Speed
    speed: Optional[bool] = None

    # Subtypes
    subtypes: Optional[list[str]] = None

    # Types
    types: Optional[list[str]] = None

    # UUID
    uuid: Optional[str] = None

    # Effect Html
    effect_html: Optional[str] = None

    # Init
    def __init__(self, data: dict):
        # Classes
        self.classes = data.get("classes")
        # CostMemory
        self.cost_memory = data.get("cost_memory")
        # CostReserve
        self.cost_reserve = data.get("cost_reserve")
        # Cost
        cost_data = data.get("cost")
        self.cost = (cost_data.get("type"), cost_data.get("value")) if cost_data is not None else None
        # Created At
        self.created_at = data.get("created_at")
        # Editions
        EditionsData = data.get("editions")
        if (EditionsData is not None) and (len(EditionsData) != 0):
            self.editions = []
            for EditionData in EditionsData:
                self.editions.append(GACardEdition(EditionData))
        #Solo Edition file for cards found in other_orientations
        OtherEditionData = data.get("edition")
        if (OtherEditionData is not None):
            self.editions = []
            self.editions.append(GACardEdition(OtherEditionData))
        # Effect
        self.effect = data.get("effect")
        # Effect Raw
        self.effect_raw = data.get("effect_raw")
        # Element
        self.element = data.get("element")
        # Elements
        self.elements = data.get("elements")
        # Flavor
        self.flavor = data.get("flavor")
        # Legality
        legalityData = data.get("legality")
        if (legalityData is not None):
            self.legality = [
                (fmt, info.get("limit", 0))
                for fmt, info in legalityData.items()
            ]
        # Level
        self.level = data.get("level")
        # Life
        self.life = data.get("life")
        # Name
        self.name = data.get("name")
        # Power
        self.power = data.get("power")
        # Reference
        referencesData = data.get("references")
        if (referencesData is not None) and (len(referencesData) != 0):
            self.references = []
            for referenceData in referencesData:
                self.references.append(Reference(referenceData))
        # Result Editions
        resultEditionsData = data.get("result_editions")
        if (resultEditionsData is not None) and (len(resultEditionsData) != 0):
            self.result_editions = []
            for resultEditionData in resultEditionsData:
                self.result_editions.append(GACardEdition(resultEditionData))
        # Rules
        rulesData = data.get("rule")
        if (rulesData is not None):
            self.rules = []
            for ruleData in rulesData:
                self.rules.append(ruleData.get("description"))
        # Slug
        self.slug = data.get("slug")
        # Speed
        self.speed = data.get("speed")
        # Subtypes
        self.subtypes = data.get("subtypes")
        # Types
        self.types = data.get("types")
        # UUID
        self.uuid = data.get("uuid")
        # Effect HTML
        self.effect_html = data.get("effect_html")

    def __str__(self) -> str:
        result = ""

        # Name
        if self.name is not None:
            result += f"Name: {self.name}\n"
        # Slug
        if self.slug is not None:
            result += f"Slug: {self.slug}\n"
        # UUID
        if self.uuid is not None:
            result += f"UUID: {self.uuid}\n"
        # Element
        if self.element is not None:
            result += f"Element: {self.element}\n"
        # Elements
        if self.elements is not None:
            result += "Elements:\n"
            for elem in self.elements:
                result += f"{elem}\n"
                result += "---------\n"
        # Classes
        if self.classes is not None:
            result += "Classes:\n"
            for c in self.classes:
                result += f"{c}\n"
                result += "---------\n"
        # Types
        if self.types is not None:
            result += "Types:\n"
            for t in self.types:
                result += f"{t}\n"
                result += "---------\n"
        # Subtypes
        if self.subtypes is not None:
            result += "Subtypes:\n"
            for st in self.subtypes:
                result += f"{st}\n"
                result += "---------\n"
        # Cost
        if self.cost is not None:
            result += f"Cost: {self.cost[0]}|{self.cost[1]}\n"
        # Cost Memory
        if self.cost_memory is not None:
            result += f"Cost Memory: {self.cost_memory}\n"
        # Cost Reserve
        if self.cost_reserve is not None:
            result += f"Cost Reserve: {self.cost_reserve}\n"
        # Durability
        if self.durability is not None:
            result += f"Durability: {self.durability}\n"
        # Level
        if self.level is not None:
            result += f"Level: {self.level}\n"
        # Life
        if self.life is not None:
            result += f"Life: {self.life}\n"
        # Power
        if self.power is not None:
            result += f"Power: {self.power}\n"
        # Speed
        if self.speed is not None:
            result += f"Speed: {self.speed}\n"
        # Effect
        if self.effect is not None:
            result += f"Effect: {self.effect}\n"
        # Effect Raw
        if self.effect_raw is not None:
            result += f"Effect Raw: {self.effect_raw}\n"
        # Effect Html
        if self.effect_html is not None:
            result += f"Effect Html: {self.effect_html}\n"
        # Flavor
        if self.flavor is not None:
            result += f"Flavor: {self.flavor}\n"
        # Rules
        if self.rules is not None:
            result += "Rules:\n"
            for rule in self.rules:
                result += f"{rule}\n"
                result += "---------\n"
        # Legality
        if self.legality is not None:
            result += "Legality:\n"
            for leg in self.legality:
                result += f"{leg[0]}|{leg[1]}\n"
                result += "---------\n"
        # References
        if self.references is not None:
            result += "References:\n"
            for ref in self.references:
                result += f"{ref}\n"
                result += "---------\n"
        # Created At
        if self.created_at is not None:
            result += f"Created At: {self.created_at}\n"
        # Editions
        if self.editions is not None and len(self.editions) != 0:
            result += "Editions:\n"
            for edition in self.editions:
                result += f"{edition}\n"
                result += "---------\n"
        # Result Editions
        if self.result_editions is not None and len(self.result_editions) != 0:
            result += "Result Editions:\n"
            for edition in self.result_editions:
                result += f"{edition}\n"
                result += "---------\n"

        return result

@dataclass
class GACardEdition:
    # Card ID
    card_id: Optional[str] = None

    # Collector Number
    collector_number: Optional[int] = None

    # Configuration
    configuration: Optional[str] = None

    # Created At
    created_at: Optional[str] = None

    # Effect
    effect: Optional[str] = None

    # Effect Raw
    effect_raw: Optional[str] = None

    # Flavor
    flavor: Optional[str] = None

    # Illustrator
    illustrator: Optional[str] = None

    # Image Link
    img_link: Optional[str] = None

    # Orientation
    orientation: Optional[str] = None

    # Rarity
    rarity: Optional[int] = None

    # Slug
    slug: Optional[str] = None

    # Thema
    thema_foil: Optional[int] = None
    thema_nonfoil: Optional[int] = None

    thema_charm_foil: Optional[int] = None
    thema_charm_nonfoil: Optional[int] = None

    thema_ferocity_foil: Optional[int] = None
    thema_ferocity_nonfoil: Optional[int] = None

    thema_grace_foil: Optional[int] = None
    thema_grace_nonfoil: Optional[int] = None

    thema_mystique_foil: Optional[int] = None
    thema_mystique_nonfoil: Optional[int] = None

    thema_valor_foil: Optional[int] = None
    thema_valor_nonfoil: Optional[int] = None

    thema_foil_dynamic: Optional[bool] = None
    thema_nonfoil_dynamic: Optional[bool] = None

    # UUID
    uuid: Optional[str] = None

    # Collaborator
    collaborators: Optional[list[str]] = None

    # Circulation Template
    circulation_template: Optional[list[CirculationTemplate]] = None

    # Circulations
    circulations: Optional[list[CirculationTemplate]] = None

    # Other Orientation
    other_orientations: Optional[list[GACardData]] = None

    # Set Info
    set_info: Optional[SetInfo] = None

    # Effect Html
    effect_html: Optional[str] = None

    # Init
    def __init__(self, data: dict):
        # Card ID
        self.card_id = data.get("card_id")
        # Collector Number
        self.collector_number = data.get("collector_number")
        # Configuration
        self.configuration = data.get("configuration")
        # Effect
        self.effect = data.get("effect")
        # Effect Raw
        self.effect_raw = data.get("effect_raw")
        # Flavor
        self.flavor = data.get("flavor")
        # Illustrator
        self.illustrator = data.get("illustrator")
        # Image Link
        self.img_link = data.get("image")
        if (self.img_link is not None):
            self.img_link = "https://api.gatcg.com" + self.img_link
        # Orientation
        self.orientation = data.get("orientation")
        # Rarity
        self.rarity = data.get("rarity")
        # Slug
        self.slug = data.get("slug")
        # Thema
        self.thema_foil = data.get("thema_foil")
        self.thema_nonfoil = data.get("thema_nonfoil")

        self.thema_charm_foil = data.get("thema_charm_foil")
        self.thema_charm_nonfoil = data.get("thema_charm_nonfoil")

        self.thema_grace_foil = data.get("thema_grace_foil")
        self.thema_grace_nonfoil = data.get("thema_grace_nonfoil")

        self.thema_ferocity_foil = data.get("thema_ferocity_foil")
        self.thema_ferocity_nonfoil = data.get("thema_ferocity_nonfoil")

        self.thema_valor_foil = data.get("thema_valor_foil")
        self.thema_valor_nonfoil = data.get("thema_valor_nonfoil")

        self.thema_foil_dynamic = data.get("thema_foil_dynamic")
        self.thema_nonfoil_dynamic = data.get("thema_nonfoil_dynamic")
        # UUID
        self.uuid = data.get("uuid")
        # Collaborators
        self.collaborators = data.get("collaborators")
        # Circulation Templates
        circulationTemplatesData = data.get("circulationTemplates")
        if (circulationTemplatesData is not None) and (len(circulationTemplatesData) != 0):
            self.circulation_template = []
            for circulationData in circulationTemplatesData:
                self.circulation_template.append(CirculationTemplate(circulationData))
        # Circulations
        circulationsData = data.get("circulations")
        if (circulationsData is not None) and (len(circulationsData) != 0):
            self.circulations = []
            for circulationData in circulationsData:
                self.circulations.append(CirculationTemplate(circulationData))
        # Other Orientations
        otherOrientationsData = data.get("other_orientations")
        if (circulationsData is not None) and (len(otherOrientationsData) != 0):
            self.other_orientations = []
            for orientationData in otherOrientationsData:
                self.other_orientations.append(GACardData(orientationData))
        # Set Info
        if (data.get("set") is not None):
            self.set_info = SetInfo(data.get("set"))
        # Effect HTML
        self.effect_html = data.get("effect_html")

    def __str__(self) -> str:
        result = ""

        # Slug
        if self.slug is not None:
            result += f"Slug: {self.slug}\n"
        # UUID
        if self.uuid is not None:
            result += f"UUID: {self.uuid}\n"
        # Card ID
        if self.card_id is not None:
            result += f"Card ID: {self.card_id}\n"
        # Collector Number
        if self.collector_number is not None:
            result += f"Collector Number: {self.collector_number}\n"
        # Configuration
        if self.configuration is not None:
            result += f"Configuration: {self.configuration}\n"
        # Rarity
        if self.rarity is not None:
            result += f"Rarity: {self.rarity}\n"
        # Orientation
        if self.orientation is not None:
            result += f"Orientation: {self.orientation}\n"
        # Illustrator
        if self.illustrator is not None:
            result += f"Illustrator: {self.illustrator}\n"
        # Image Link
        if self.img_link is not None:
            result += f"Image Link: {self.img_link}\n"
        # Effect
        if self.effect is not None:
            result += f"Effect: {self.effect}\n"
        # Effect Raw
        if self.effect_raw is not None:
            result += f"Effect Raw: {self.effect_raw}\n"
        # Effect Html
        if self.effect_html is not None:
            result += f"Effect Html: {self.effect_html}\n"
        # Flavor
        if self.flavor is not None:
            result += f"Flavor: {self.flavor}\n"
        # Created At
        if self.created_at is not None:
            result += f"Created At: {self.created_at}\n"
        # Thema
        if self.thema_foil is not None:
            result += f"Thema Foil: {self.thema_foil}\n"
        if self.thema_nonfoil is not None:
            result += f"Thema Nonfoil: {self.thema_nonfoil}\n"
        if self.thema_charm_foil is not None:
            result += f"Thema Charm Foil: {self.thema_charm_foil}\n"
        if self.thema_charm_nonfoil is not None:
            result += f"Thema Charm Nonfoil: {self.thema_charm_nonfoil}\n"
        if self.thema_ferocity_foil is not None:
            result += f"Thema Ferocity Foil: {self.thema_ferocity_foil}\n"
        if self.thema_ferocity_nonfoil is not None:
            result += f"Thema Ferocity Nonfoil: {self.thema_ferocity_nonfoil}\n"
        if self.thema_grace_foil is not None:
            result += f"Thema Grace Foil: {self.thema_grace_foil}\n"
        if self.thema_grace_nonfoil is not None:
            result += f"Thema Grace Nonfoil: {self.thema_grace_nonfoil}\n"
        if self.thema_mystique_foil is not None:
            result += f"Thema Mystique Foil: {self.thema_mystique_foil}\n"
        if self.thema_mystique_nonfoil is not None:
            result += f"Thema Mystique Nonfoil: {self.thema_mystique_nonfoil}\n"
        if self.thema_valor_foil is not None:
            result += f"Thema Valor Foil: {self.thema_valor_foil}\n"
        if self.thema_valor_nonfoil is not None:
            result += f"Thema Valor Nonfoil: {self.thema_valor_nonfoil}\n"
        if self.thema_foil_dynamic is not None:
            result += f"Thema Foil Dynamic: {self.thema_foil_dynamic}\n"
        if self.thema_nonfoil_dynamic is not None:
            result += f"Thema Nonfoil Dynamic: {self.thema_nonfoil_dynamic}\n"
        # Collaborators
        if self.collaborators is not None:
            result += "Collaborators:\n"
            for collab in self.collaborators:
                result += f"{collab}\n"
                result += "---------\n"
        # Circulation Template
        if self.circulation_template is not None:
            result += "Circulation Templates:\n"
            for ct in self.circulation_template:
                result += f"{ct}\n"
                result += "---------\n"
        # Circulations
        if self.circulations is not None:
            result += "Circulations:\n"
            for circ in self.circulations:
                result += f"{circ}\n"
                result += "---------\n"
        # Other Orientations
        if self.other_orientations is not None:
            result += "Other Orientations:\n"
            for orientation in self.other_orientations:
                result += f"Name: {orientation.name}\n"
                result += "---------\n"
        # Set Info
        if self.set_info is not None:
            result += f"Set Info: {self.set_info}\n"

        return result