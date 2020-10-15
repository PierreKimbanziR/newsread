# Newsread 

## What? 
News Web application. I used [Django](https://www.djangoproject.com/) for the backend logic and [bootstrap4](https://getbootstrap.com/) for my templates. 
The differents news articles are collected using [NewsApi](https://newsapi.org/).

## User registration
It is possible to use the site without creating a user profile, but it is recommended to create one. Indeed, creating one allows you to choose the newspapers you wish to be displayed.
A system of password reset by email has also been implemented. You just have to enter your email adress and a mail containing a reset link will be sent. Note that the adress mail has to mach the one used when creating your profile. 

## Django Auth.views
All of the views relating to the authentication process are based on the built-in [django auth-views](https://docs.djangoproject.com/fr/1.8/_modules/django/contrib/auth/views/) .
