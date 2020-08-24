
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
import requests_with_caching
import json

def get_movies_from_tastedive(title):
    endpoint = "https://tastedive.com/api/similar"
    param = dict()
    param['q'] = title
    param['type'] = 'movies'
    param['limit'] = 5

    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)



def extract_movie_titles(movies):
    return [name['Name'] for name in movies['Similar']['Results']]

def get_related_titles(movies_title):
    ls = []
    for movie in movies_title:
        ls.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(ls))

get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])
