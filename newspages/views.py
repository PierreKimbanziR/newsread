import os
from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def Bbc(request):
    api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key)
    headlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = headlines['articles']
    description =  []
    news = []
    images = []
    links_to_article = []
    journal_name = articles[0]['source']['name']


    for i in range(len(articles)):
        set_of_articles = articles[i]

        description.append(set_of_articles['description'])
        news.append(set_of_articles['title'])
        images.append(set_of_articles['urlToImage'])
        links_to_article.append(set_of_articles['url'])

    news_list = zip(news, description, images, links_to_article)

    return render(request, 'newspages/news.html', context={"news_list":news_list, "journal_name":journal_name})

def Abc_News(request):
    api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key)
    headlines = newsapi.get_top_headlines(sources="abc-news")

    articles = headlines['articles']
    description =  []
    news = []
    images = []
    links_to_article = []
    journal_name = articles[0]['source']['name']


    for i in range(len(articles)):
        set_of_articles = articles[i]

        description.append(set_of_articles['description'])
        news.append(set_of_articles['title'])
        images.append(set_of_articles['urlToImage'])
        links_to_article.append(set_of_articles['url'])


    news_list = zip(news, description, images, links_to_article)

    return render(request, 'newspages/news.html', context={"news_list":news_list, "journal_name":journal_name})

def AP(request):
    api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key)
    headlines = newsapi.get_top_headlines(sources="associated-press")

    articles = headlines['articles']
    description =  []
    news = []
    images = []
    links_to_article = []
    journal_name = articles[0]['source']['name']


    for i in range(len(articles)):
        set_of_articles = articles[i]

        description.append(set_of_articles['description'])
        news.append(set_of_articles['title'])
        images.append(set_of_articles['urlToImage'])
        links_to_article.append(set_of_articles['url'])


    news_list = zip(news, description, images, links_to_article)

    return render(request, 'newspages/news.html', context={"news_list":news_list, "journal_name":journal_name})

def home(request):
    api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key)
    headlines = newsapi.get_top_headlines(sources='bbc-sport')


    articles = headlines['articles']
    description =  []
    news = []
    images = []
    links_to_article = []
    journal_name = articles[0]['source']['name']

    for i in range(len(articles)):
        set_of_articles = articles[i]

        description.append(set_of_articles['description'])
        news.append(set_of_articles['title'])
        images.append(set_of_articles['urlToImage'])
        links_to_article.append(set_of_articles['url'])
    news_list = zip(news, description, images, links_to_article)





    return render(request, 'newspages/home.html', context={"news_list": news_list, "journal_name": journal_name})

