from django.urls import path
from .views import *
app_name = 'polls'  #polls:index
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:question_id>/',detail, name="detail"),
    path('<str:question_id>/vote', vote, name="vote"),
    path('<int:pk>/result',ResultsView.as_view(), name="result")

]
