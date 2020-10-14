import os
from newsapi import NewsApiClient


def get_sources_list():
    api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key)
    full_sources = newsapi.get_sources()
    sources = full_sources['sources']
    list_of_sources = []

    for i in range (len(sources)):
        source = sources[i]
        source_name = source["name"]
        source_id = source['id']

        list_of_sources.append((source_id, source_name))
        tuple_of_sources = tuple(list_of_sources)
    return(tuple_of_sources)

get_sources_list()

