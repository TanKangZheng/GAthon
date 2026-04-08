import enums
import field
from dataclasses import dataclass
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
    element = Optional[str] = None

    # Elements
    elements = Optional[list[str]] = None

    # Flavor
    flavor = Optional[str] = None

    # Legality
    legality = Optional[list[tuple[str, int]]] = None #str = Format, int = limit

    # Level
    level = Optional[int] = None

    # Life
    life = Optional[int] = None

    # Name
    name = Optional[str] = None

    # Power
    power = Optional[int] = None

    # References
    references = Optional[list[Reference]] = None

    # Result Editions
    result_editions = Optional[list["GACardEdition"]] = field(default_factory=list)

    # Rules
    rules = Optional[list[str]] = None

    # Slug
    slug = Optional[str] = None

    # Speed
    speed = Optional[bool] = None

    # Subtypes
    subtypes = Optional[list[str]] = None

    # Types
    types = Optional[list[str]] = None

    # UUID
    uuid = Optional[str] = None

    # Effect Html
    effect_html = Optional[str] = None

    # Init
    def __init__(self, data: dict):
        # Classes
        self.classes = data.get("classes")
        # CostMemory
        self.cost_memory = data.get("cost_memory")
        # CostReserve
        self.cost_reserve = data.get("cost_reserve")
        # Cost
        self.cost = (data.get("cost")[0], data.get("cost")[1])
        # Created At
        self.created_at = data.get("created_at")
        # Editions
        # TODO
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
        self.legality = [
            (fmt, info.get("limit", 0))
            for fmt, info in data.get("legality", {}).items()
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
        # TODO
        # Result Editions
        # TODO
        # Rules
        self.rules = data.get("rules")
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
        if (len(circulationTemplatesData) is not 0):
            self.circulation_template = []
            for circulationData in circulationTemplatesData:
                self.circulation_template.append(CirculationTemplate(circulationTemplatesData))
        # Circulations
        circulationsData = data.get("circulations")
        if (len(circulationsData) is not 0):
            self.circulations = []
            for circulationData in circulationsData:
                self.circulation_template.append(CirculationTemplate(circulationData))
        # Other Orientations
        # TODO