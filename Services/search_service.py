import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Data.repository import Repo
from typing import List, Dict, Any

class SearchService:
    def __init__(self):
        self.repo = Repo()

    def search_manga(self, filters: Dict[str, Any]) -> List[str]:
        return self.repo.search(
            genre=filters.get("genre"),
            tag=filters.get("tag"),
            theme=filters.get("theme"),
            author=filters.get("author"),
            artist=filters.get("artist"),
            title=filters.get("title"),
            exclude_genre=filters.get("exclude_genre"),
            exclude_tag=filters.get("exclude_tag"),
            exclude_theme=filters.get("exclude_theme"),
            exclude_title=filters.get("exclude_title"),
            exclude_format=filters.get("exclude_format"),
            min_rating=filters.get("min_rating"),
            max_rating=filters.get("max_rating"),
            published_before=filters.get("published_before"),
            published_after=filters.get("published_after"),
            origination=filters.get("origination"),
            demographic=filters.get("demographic"),
            anime=filters.get("anime"),
            format=filters.get("format"),
            status=filters.get("status"),
            official_translation=filters.get("official_translation"),
            fan_translation=filters.get("fan_translation"),
            min_fan_translated=filters.get("min_fan_translated"),
            max_fan_translated=filters.get("max_fan_translated"),
            min_number_together=filters.get("min_number_together"),
            max_number_together=filters.get("max_number_together"),
            limit=filters.get("limit", 50),
            offset=filters.get("offset", 0)
        )
        

    def get_manga_details(self, comick_link: str) -> Dict[str, Any]:
        return {
            "basic": self.repo.dobi_basic_info(comick_link),
            "titles": self.repo.dobi_titles(comick_link),  
            "tags": self.repo.dobi_tags(comick_link),
            "genres": self.repo.dobi_genres(comick_link),
            "themes": self.repo.dobi_themes(comick_link),
            "authors": self.repo.dobi_authors(comick_link),
            "artists": self.repo.dobi_artists(comick_link),
            "rating": self.repo.dobi_ratings(comick_link),
            "cover": self.repo.dobi_cover_url(comick_link),
            "translation": self.repo.dobi_translation(comick_link),
            "description": self.repo.dobi_description(comick_link),
        }
    
    def get_banned(self) -> Dict[str, Any]:
        return {
            "banned_themes": self.repo.dobi_banned_themes(),
            "banned_genres": self.repo.dobi_banned_genres(),  
            "banned_format": self.repo.dobi_banned_format(),
            "banned_tag": self.repo.dobi_banned_tag(),
        }
        
   