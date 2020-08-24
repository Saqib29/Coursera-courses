
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


def get_movie_data(title):
    endpoint = "http://www.omdbapi.com/"
    param = dict()
    param['t'] = title
    param['r'] = 'json'
    
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

def get_movie_rating(dict_data):
    for rating in dict_data['Ratings']:
        if rating['Source'] == "Rotten Tomatoes":
            return int(rating['Value'][:-1])
    return 0

def get_sorted_recommendations(movie_list):
    movies_titles_list = get_related_titles(movie_list)
    movies_dic = dict()
    for movie in movies_titles_list:
        movies_dic[movie] = get_movie_rating(get_movie_data(movie))
    
    sorted_movies = [i[0] for i in sorted(movies_dic.items(), key=lambda items: (items[1], items[0]), reverse=True)]
    return sorted_movies
        
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

