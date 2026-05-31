import psycopg2
import psycopg2.extras
from Data import auth_public as auth
from typing import List

from Data.models import (
    linki, basic_info, tags, translation, description,
    relations, recommendations, genres, titles, themes,
    authors, artists, ratings, users, reading, clicks, searches
)


class Repo:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=auth.db,
            host=auth.host,
            user=auth.user,
            password=auth.password,
            port=auth.port
        )
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


    def dobi_linki(self, comick_link: str) -> linki:
        self.cur.execute("SELECT * FROM linki WHERE comick_link = %s", (comick_link,))
        row = self.cur.fetchone()
        return linki.from_dict(row) if row else None


    def dobi_basic_info(self, comick_link: str) -> basic_info:
        self.cur.execute("SELECT * FROM basic_info WHERE comick_link = %s", (comick_link,))
        row = self.cur.fetchone()
        return basic_info.from_dict(row) if row else None


    def dobi_tags(self, comick_link: str) -> List[tags]:
        self.cur.execute("SELECT * FROM tags WHERE comick_link = %s", (comick_link,))
        return [tags.from_dict(r) for r in self.cur.fetchall()]


    def dobi_translation(self, comick_link: str) -> translation:
        self.cur.execute("SELECT * FROM translation WHERE comick_link = %s", (comick_link,))
        row = self.cur.fetchone()
        return translation.from_dict(row) if row else None


    def dobi_description(self, comick_link: str) -> description:
        self.cur.execute("SELECT * FROM description WHERE comick_link = %s", (comick_link,))
        row = self.cur.fetchone()
        return description.from_dict(row) if row else None


    def dobi_relations(self, comick_link: str) -> List[relations]:
        self.cur.execute("SELECT * FROM relations WHERE comick_link = %s", (comick_link,))
        return [relations.from_dict(r) for r in self.cur.fetchall()]


    def dobi_recommendations(self, comick_link: str) -> List[recommendations]:
        self.cur.execute("SELECT * FROM recommendations WHERE comick_link = %s", (comick_link,))
        return [recommendations.from_dict(r) for r in self.cur.fetchall()]


    def dobi_genres(self, comick_link: str) -> List[genres]:
        self.cur.execute("SELECT * FROM genres WHERE comick_link = %s", (comick_link,))
        return [genres.from_dict(r) for r in self.cur.fetchall()]


    def dobi_titles(self, comick_link: str) -> List[titles]:
        self.cur.execute("SELECT * FROM titles WHERE comick_link = %s", (comick_link,))
        return [titles.from_dict(r) for r in self.cur.fetchall()]


    def dobi_themes(self, comick_link: str) -> List[themes]:
        self.cur.execute("SELECT * FROM themes WHERE comick_link = %s", (comick_link,))
        return [themes.from_dict(r) for r in self.cur.fetchall()]


    def dobi_authors(self, comick_link: str) -> List[authors]:
        self.cur.execute("SELECT * FROM authors WHERE comick_link = %s", (comick_link,))
        return [authors.from_dict(r) for r in self.cur.fetchall()]


    def dobi_artists(self, comick_link: str) -> List[artists]:
        self.cur.execute("SELECT * FROM artists WHERE comick_link = %s", (comick_link,))
        return [artists.from_dict(r) for r in self.cur.fetchall()]


    def dobi_ratings(self, comick_link: str) -> ratings:
        self.cur.execute("SELECT * FROM ratings WHERE comick_link = %s", (comick_link,))
        row = self.cur.fetchone()
        return ratings.from_dict(row) if row else None


    def dobi_cover_url(self, comick_link: str) -> str:
        self.cur.execute(
            "SELECT cover_url FROM linki WHERE comick_link = %s",
            (comick_link,)
        )
        row = self.cur.fetchone()
        return row["cover_url"] if row else None


    def search(
        self,
        genre: str = None,
        tag: str = None,
        theme: str = None,
        author: str = None,
        artist: str = None,
        title: str = None,

        min_rating: float = None,
        max_rating: float = None,

        published_before: int = None,
        published_after: int = None,

        origination: str = None,
        demographic: int = None,
        anime: bool = None,
        format: str = None,
        status: int = None,

        official_translation: bool = None,
        fan_translation: bool = None,

        min_fan_translated: float = None,
        max_fan_translated: float = None,

        min_number_together: float = None,
        max_number_together: float = None,

        limit: int = 50,
        offset: int = 0
    ) -> list[str]:

        query = """
            SELECT DISTINCT l.comick_link
            FROM linki l
            LEFT JOIN basic_info b ON l.comick_link = b.comick_link
            LEFT JOIN ratings r ON l.comick_link = r.comick_link
            LEFT JOIN translation tr ON l.comick_link = tr.comick_link
            WHERE 1=1
        """

        params = []

        if genre:     
            genre_list = [g.strip() for g in genre.split(',') if g.strip()]
            for g in genre_list:
                query += " AND EXISTS (SELECT 1 FROM genres g WHERE g.comick_link = l.comick_link AND LOWER(g.genre) = LOWER(%s))"
                params.append(g)

        if tag:
            tag_list = [t.strip() for t in tag.split(',') if t.strip()]
            for t in tag_list:
                query += " AND EXISTS (SELECT 1 FROM tags t WHERE t.comick_link = l.comick_link AND LOWER(t.tag) = LOWER(%s))"
                params.append(t)

        if theme:
            theme_list = [th.strip() for th in theme.split(',') if th.strip()]
            for th in theme_list:
                query += " AND EXISTS (SELECT 1 FROM themes th WHERE th.comick_link = l.comick_link AND LOWER(th.themes) = LOWER(%s))"
                params.append(th)

        if author:
            query += " AND EXISTS (SELECT 1 FROM authors a WHERE a.comick_link = l.comick_link AND LOWER(a.author) = LOWER(%s))"
            params.append(author)

        if artist:
            query += " AND EXISTS (SELECT 1 FROM artists ar WHERE ar.comick_link = l.comick_link AND LOWER(ar.artist) = LOWER(%s))"
            params.append(artist)

        if title:
            query += " AND EXISTS (SELECT 1 FROM titles ti WHERE ti.comick_link = l.comick_link AND LOWER(ti.title) LIKE LOWER(%s))"
            params.append(f"%{title}%")

        if min_rating is not None:
            query += " AND r.bay_rating >= %s"
            params.append(min_rating)

        if max_rating is not None:
            query += " AND r.bay_rating <= %s"
            params.append(max_rating)

        if published_before is not None:
            query += " AND b.published <= %s"
            params.append(published_before)

        if published_after is not None:
            query += " AND b.published >= %s"
            params.append(published_after)

        if origination:
            query += " AND LOWER(b.origination) = LOWER(%s)"
            params.append(origination)

        if demographic is not None:
            query += " AND b.demographic = %s"
            params.append(demographic)

        if anime is not None:
            query += " AND b.anime = %s"
            params.append(anime)

        if format:
            query += " AND LOWER(b.format) = LOWER(%s)"
            params.append(format)

        if status is not None:
            query += " AND b.status = %s"
            params.append(status)

        # Translation pogoji (1:1 tabela)
        if official_translation is not None:
            query += " AND tr.official_translation = %s"
            params.append(official_translation)

        if fan_translation is not None:
            query += " AND tr.fan_translation = %s"
            params.append(fan_translation)

        if min_fan_translated is not None:
            query += " AND tr.number_fan_translated >= %s"
            params.append(min_fan_translated)

        if max_fan_translated is not None:
            query += " AND tr.number_fan_translated <= %s"
            params.append(max_fan_translated)

        if min_number_together is not None:
            query += " AND tr.number_together >= %s"
            params.append(min_number_together)

        if max_number_together is not None:
            query += " AND tr.number_together <= %s"
            params.append(max_number_together)

        query += " ORDER BY l.comick_link LIMIT %s OFFSET %s"
        params.extend([limit, offset])

        self.cur.execute(query, tuple(params))
        return [r["comick_link"] for r in self.cur.fetchall()]





  