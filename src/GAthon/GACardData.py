import enums
import field
from dataclasses import dataclass
from typing import Optional

@dataclass
class CirculationTemplate:
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

@dataclass
class SetInfo:
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

@dataclass
class GACardData:
    # Classes
    classes: Optional[list[str]] = None

    # Cost
    cost_memory: Optional[int] = None
    cost_reserve: Optional[int] = None

    # Durability
    cost_durability: Optional[int] = None

    # Editions
    editions: Optional[list["GACardEdition"]] = field(default_factory=list)

    # Effect
    effect: Optional[str] = None

    # Effect Raw
    effect_raw: Optional[str] = None

    # Element
    element = Optional[str] = None

    # Flavor
    flavor = Optional[str] = None

    # Legality
    legality = Optional[str] = None

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
    speed = Optional[str] = None

    # Subtypes
    subtypes = Optional[list[str]] = None

    # Types
    types = Optional[list[str]] = None

    # UUID
    uuid = Optional[str] = None

    # Effect Html
    effect_html = Optional[str] = None

@dataclass
class GACardEdition:
    # Card ID
    card_id: Optional[str] = None

    # Collector Number
    collector_number: Optional[int] = None

    # Configuration
    configuration: Optional[str] = None

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
