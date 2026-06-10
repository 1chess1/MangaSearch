import sys
import os

#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bottle import Bottle, request, template, static_file
from Services.search_service import SearchService

app = Bottle()
search_service = SearchService()

template_lookup = [os.path.join(os.path.dirname(__file__), 'views')]

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./Presentation/static')

@app.route('/')
@app.route('/search')
def search_form():
    banned_items = search_service.get_banned()
    return template('search', 
                   results=[], 
                   filters={}, 
                   banned_items=banned_items,
                   template_lookup=template_lookup)


@app.route('/search', method='POST')
def search_submit():
    exclude_18plus_bool = request.forms.get("exclude_18plus") == "true"
    
    raw_filters = {
        "title": request.forms.get("title") or None,
        "author": request.forms.get("author") or None,
        "artist": request.forms.get("artist") or None,
        "genre": request.forms.get("genre") or None,
        "tag": request.forms.get("tag") or None,
        "theme": request.forms.get("theme") or None,
        "exclude_title": request.forms.get("exclude_title") or None,
        "exclude_genre": request.forms.get("exclude_genre") or None,
        "exclude_tag": request.forms.get("exclude_tag") or None,
        "exclude_theme": request.forms.get("exclude_theme") or None,
        "min_rating": float(request.forms.get("min_rating")) if request.forms.get("min_rating") else None,
        "max_rating": float(request.forms.get("max_rating")) if request.forms.get("max_rating") else None,
        "published_after": int(request.forms.get("published_after")) if request.forms.get("published_after") else None,
        "published_before": int(request.forms.get("published_before")) if request.forms.get("published_before") else None,
        "origination": request.forms.get("origination") or None,
        "demographic": int(request.forms.get("demographic")) if request.forms.get("demographic") else None,
        "anime": request.forms.get("anime") == "true" if request.forms.get("anime") else None,
        "format": request.forms.get("format") or None,
        "status": int(request.forms.get("status")) if request.forms.get("status") else None,
        "official_translation": request.forms.get("official_translation") == "true" if request.forms.get("official_translation") else None,
        "fan_translation": request.forms.get("fan_translation") == "true" if request.forms.get("fan_translation") else None,
        "min_fan_translated": float(request.forms.get("min_fan_translated")) if request.forms.get("min_fan_translated") else None,
        "max_fan_translated": float(request.forms.get("max_fan_translated")) if request.forms.get("max_fan_translated") else None,
        "min_number_together": float(request.forms.get("min_number_together")) if request.forms.get("min_number_together") else None,
        "max_number_together": float(request.forms.get("max_number_together")) if request.forms.get("max_number_together") else None,
        "limit": int(request.forms.get("limit", 50)),
        "offset": int(request.forms.get("offset", 0)),
    }
    
    filters = {k: v for k, v in raw_filters.items() if v is not None and v != ""}
    
    display_filters = filters.copy()
    display_filters["exclude_18plus"] = exclude_18plus_bool
    
    if exclude_18plus_bool:
        banned = search_service.get_banned()
        
        if banned["banned_genres"]:
            existing = filters.get("exclude_genre", "")
            existing_list = [g.strip() for g in existing.split(",")] if existing else []
            for bg in banned["banned_genres"]:
                if bg not in existing_list:
                    existing_list.append(bg)
            filters["exclude_genre"] = ",".join(existing_list) if existing_list else None
        
        if banned["banned_tag"]:
            existing = filters.get("exclude_tag", "")
            existing_list = [t.strip() for t in existing.split(",")] if existing else []
            for bt in banned["banned_tag"]:
                if bt not in existing_list:
                    existing_list.append(bt)
            filters["exclude_tag"] = ",".join(existing_list) if existing_list else None
        
        if banned["banned_themes"]:
            existing = filters.get("exclude_theme", "")
            existing_list = [th.strip() for th in existing.split(",")] if existing else []
            for bth in banned["banned_themes"]:
                if bth not in existing_list:
                    existing_list.append(bth)
            filters["exclude_theme"] = ",".join(existing_list) if existing_list else None
        
        if banned["banned_format"]:
            existing = filters.get("exclude_format", "")
            existing_list = [f.strip() for f in existing.split(",")] if existing else []
            for bf in banned["banned_format"]:
                if bf not in existing_list:
                    existing_list.append(bf)
            filters["exclude_format"] = ",".join(existing_list) if existing_list else None
    
    results = search_service.search_manga(filters)
    banned_items = search_service.get_banned()
    
    return template('search', 
                   results=results, 
                   filters=display_filters,
                   banned_items=banned_items,
                   template_lookup=template_lookup)





@app.route('/manga/<path:path>')
def manga_details(path):
    comick_link = path
    details = search_service.get_manga_details(comick_link)
    
    if not details["basic"]:
        return template('404', link=comick_link, template_lookup=template_lookup)
    
    return template('manga_details', 
                   link=comick_link,
                   basic=details["basic"],
                   titles=details["titles"],
                   tags=details["tags"],
                   themes=details["themes"], 
                   genres=details["genres"],
                   authors=details["authors"],
                   artists=details["artists"],
                   rating=details["rating"],
                   cover=details["cover"],
                   translation=details["translation"],
                   description=details["description"],
                   template_lookup=template_lookup)
    
    
@app.route('/info')
def show_info():
    tag_search = request.query.get('tag_search', '').strip()
    info = search_service.get_info(tag_search=tag_search)
    return template('info',
                   tags=info.get('tag'),
                   genres=info.get('genres'),
                   themes=info.get('themes'),
                   tag_search=tag_search,
                   template_lookup=template_lookup)

@app.error(404)
def error404(error):
    return template('cute', template_lookup=template_lookup)


