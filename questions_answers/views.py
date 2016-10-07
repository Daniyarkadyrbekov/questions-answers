import django.views.generic


class GetTempPage(django.views.generic.TemplateView):
    template_name = 'main_app/pages/temp.html'


class GetNewQuestions(django.views.generic.TemplateView):
    template_name = 'main_app/pages/new_questions_page.html'


class GetNewQuestionList(django.views.generic.TemplateView):
    template_name = 'main_app/pages/new_question_page.html'


class GetQuestionDetailList(django.views.generic.TemplateView):
    template_name = 'main_app/pages/question_detail_page.html'


class GetTagQuestions(django.views.generic.TemplateView):
    template_name = 'main_app/pages/tag_question_page.html'


class GetUserSettings(django.views.generic.TemplateView):
    template_name = 'main_app/pages/user_settings_page.html'


class GetLoginPage(django.views.generic.TemplateView):
    template_name = 'main_app/pages/login_page.html'


class GetRegistrationPage(django.views.generic.TemplateView):
    template_name = 'main_app/pages/registration_page.html'


class GetNotLogged(django.views.generic.TemplateView):
    template_name = 'main_app/pages/not_logged_new_questions_page.html'