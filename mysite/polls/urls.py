from django.urls import path
from . import views

# namespacing the URL's
app_name = 'polls'
urlpatterns = [
    #We use Generic Views Instead of the first ones we create
    #path('', views.index, name='index'),
    path('', views.index, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('newPoll/', views.PollFormTemplate, name='newPoll'),
    path('savePoll/', views.SavePoll, name='savePoll')
]