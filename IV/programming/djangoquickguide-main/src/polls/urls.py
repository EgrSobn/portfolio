# Пути для приложения polls
from django.urls import path

from . import views

app_name = "polls"
#path(маршрут в адресной строке, функция в views.DefName, name="DefName")
urlpatterns = [
    # /polls/
    # path("", views.index, name="index"),

    # # /polls/NumberOfQuestion/
    # path("<int:question_id>/", views.detail, name="detail"),

    # # /polls/NumberOfQuestion/results/
    # path("<int:question_id>/result/", views.result, name="result"),

    path("", views.IndexView.as_view(), name='index'),

    path("<int:pk>/", views.DetailView.as_view(), name='detail'),

    path("<int:pk>/results", views.ResultsView.as_view(), name="result"),
    
    # /polls/NumberOfQuestion/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

]
