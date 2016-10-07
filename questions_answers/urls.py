"""questions_answers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^temp/', views.GetTempPage.as_view(), name='temp_page'),
    url(r'^new/', views.GetNewQuestions.as_view(), name='new'),
    url(r'^new_question/', views.GetNewQuestionList.as_view(), name='new_question'),
    url(r'^question_detail/', views.GetQuestionDetailList.as_view(), name='question_detail'),
    url(r'^tag_question/', views.GetTagQuestions.as_view(), name='tag_question'),
    url(r'^user_settings/', views.GetUserSettings.as_view(), name='user_settings'),
    url(r'^login/', views.GetLoginPage.as_view(), name='login'),
    url(r'^registration/', views.GetRegistrationPage.as_view(), name='registration'),
    url(r'^not_logged/', views.GetNotLogged.as_view(), name='not_logged'),
]
