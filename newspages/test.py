import os
from django.shortcuts import render
from newsapi import NewsApiClient

def Bbc():
    api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key)
    headlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = headlines['articles']
    journal = articles[0]['source']['name']
    print(journal)
Bbc()