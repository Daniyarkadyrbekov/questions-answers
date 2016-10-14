import django.views.generic


class GetNewQuestions(django.views.generic.TemplateView):
    template_name = 'pages/new_questions_page.html'


class GetNewQuestionList(django.views.generic.TemplateView):
    template_name = 'pages/new_question_page.html'


class GetQuestionDetailList(django.views.generic.TemplateView):
    template_name = 'pages/question_detail_page.html'


class GetTagQuestions(django.views.generic.TemplateView):
    template_name = 'pages/tag_question_page.html'


class GetUserSettings(django.views.generic.TemplateView):
    template_name = 'pages/user_settings_page.html'


class GetLoginPage(django.views.generic.TemplateView):
    template_name = 'pages/login_page.html'


class GetRegistrationPage(django.views.generic.TemplateView):
    template_name = 'pages/registration_page.html'


class GetNotLogged(django.views.generic.TemplateView):
    template_name = 'pages/not_logged_new_questions_page.html'
