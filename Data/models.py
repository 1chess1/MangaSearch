from dataclasses import dataclass, field
from dataclasses_json import dataclass_json




@dataclass_json
@dataclass
class basic_info:
    comick_link: str = field(default="")
    origination: str = field(default="")
    demographic: int = field(default=0)
    published: int = field(default=0)
    status: int = field(default=0)
    format: str = field(default="")
    anime: bool = field(default=False)



@dataclass_json
@dataclass
class tags:
    comick_link: str = field(default="")
    tag: str = field(default="")



@dataclass_json
@dataclass
class translation:
    comick_link: str = field(default="")
    official_translation: bool = field(default=False)
    fan_translation: bool = field(default=False)
    number_fan_translated: float = field(default=0)
    number_together: float = field(default=0)



@dataclass_json
@dataclass
class description:
    id: int = field(default=0)
    comick_link: str = field(default="")
    description: str = field(default="")




@dataclass_json
@dataclass
class genres:
    comick_link: str = field(default="")
    genre: str = field(default="")



@dataclass_json
@dataclass
class titles:
    comick_link: str = field(default="")
    title: str = field(default="")



@dataclass_json
@dataclass
class themes:
    comick_link: str = field(default="")
    themes: str = field(default="")



@dataclass_json
@dataclass
class authors:
    id: int = field(default=0)
    comick_link: str = field(default="")
    author: str = field(default="")



@dataclass_json
@dataclass
class artists:
    id: int = field(default=0)
    comick_link: str = field(default="")
    artist: str = field(default="")



@dataclass_json
@dataclass
class ratings:
    comick_link: str = field(default="")
    ranked: int = field(default=0)
    followed: int = field(default=0)
    bay_rating: float = field(default=0)



    
@dataclass_json
@dataclass
class banned:
    name: str = field(default="")
    type: str = field(default="")

    


