from dataclasses import dataclass, field
from dataclasses_json import dataclass_json



@dataclass_json
@dataclass
class linki:
    id: int = field(default=0)
    comick_link: str = field(default="")

    al_link: str = field(default="")
    ap_link: str = field(default="")
    mu_link: str = field(default="")
    raw_link: str = field(default="")
    mb_link: str = field(default="")
    bw_link: str = field(default="")
    mal_link: str = field(default="")
    md_link: str = field(default="")
    cover_url: str = field(default="")



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
class relations:
    comick_link: str = field(default="")
    related_link: str = field(default="")



@dataclass_json
@dataclass
class recommendations:
    comick_link: str = field(default="")
    recommended_link: str = field(default="")



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
class users:
    user_id: int = field(default=0)
    username: str = field(default="")
    email: str = field(default="")
    password: str = field(default="")



@dataclass_json
@dataclass
class reading:
    reading_id: int = field(default=0)
    user_id: int = field(default=0)
    comick_link: str = field(default="")



@dataclass_json
@dataclass
class clicks:
    clicks_id: int = field(default=0)
    user_id: int = field(default=0)
    clicked_link: str = field(default="")



@dataclass_json
@dataclass
class searches:
    searches_id: int = field(default=0)
    user_id: int = field(default=0)
    searched: str = field(default="")



@dataclass_json
@dataclass
class user_analysis:
    user_id: int = field(default=0)

    gender_count: int = field(default=0)
    gender_guess: str = field(default="")

    age_count: int = field(default=0)
    age_guess: int = field(default=0)

    user_rank_genres_count: int = field(default=0)
    user_rank_genres: int = field(default=0)

    user_rank_title_count: int = field(default=0)
    user_rank_title: int = field(default=0)

    user_rank_quality_count: int = field(default=0)
    user_rank_quality: int = field(default=0)

    user_rank: int = field(default=0)

    danger_count: int = field(default=0)
    danger_alert: bool = field(default=False)
    bot_alert: bool = field(default=False)

    a_rank: int = field(default=0)
    a_count: int = field(default=0)
    
@dataclass_json
@dataclass
class banned:
    name: str = field(default="")
    type: str = field(default="")

    


