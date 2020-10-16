from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
from .forms import MediaSelectionForm
from django.contrib.auth.decorators import login_required
from .MODEL_API_CALL import get_personal_medias


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form':form})

# Creating the form to allow users to select the news that they want to see displayed on their personal homepage

@login_required
def mediaselection(request):

    if request.method == 'POST':
            form = MediaSelectionForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user =request.user
                instance.save()
                messages.success(request, f'Your favorites media have beeen saved.')
                return redirect('home')
    else:
        form = MediaSelectionForm()



    return render(request, 'users/media_selection_form.html', {'form':form})


def personal_page(request):
    list_of_headlines_to_display = get_personal_medias()
    list_of_news =[]
    journal_names= []

    for headlines in list_of_headlines_to_display:
        articles = headlines['articles']

        description =  []
        news = []
        images = []
        links_to_article = []
        journal_names.append(articles[0]['source']['name'])
        print(journal_names)

        for i in range(len(articles)):
            set_of_articles = articles[i]
            description.append(set_of_articles['description'])
            news.append(set_of_articles['title'])
            images.append(set_of_articles['urlToImage'])
            links_to_article.append(set_of_articles['url'])


        news_list = zip(news, description, images, links_to_article)
        list_of_news.append(news_list)
        complete_list = zip(list_of_news, journal_names)


    return render(request, 'users/personal_page.html', context={'complete_list': complete_list})
