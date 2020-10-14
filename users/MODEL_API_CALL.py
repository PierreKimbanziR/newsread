import os
from newsapi import NewsApiClient
from .models import MediaList

def get_personal_medias():
    api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key)

    liste = MediaList.objects.get(id=1)
    medias = liste.medias
    list_of_headlines = []
    for item in medias:
        top_headlines = newsapi.get_top_headlines(sources=item)
        list_of_headlines.append(top_headlines)

    return list_of_headlines
get_personal_medias()


    
def get_sources_id():
    api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key)

    sources = newsapi.get_sources()
    # print (sources['sources'])

