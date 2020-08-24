import requests_with_caching
import json

pareameters = {"term": "Ann Arbor", "entity": "podcast"}

iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params=pareameters, permanent_cache_file = "itunes_cache/itunes_cache.txt")

py_data = json.loads(iTunes_response.text)