from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post.netlify.app', views.create_post, name='create_post'),
    path('creating.netlify.app', views.creating, name='create'),
    path('delete/<int:id>.netlify.app', views.delete_post, name='delete_post'),
    path('just_redact/<int:id>.netlify.app', views.just_redact, name='just_redact'),
    path('redacting/<int:id>.netlify.app', views.redacting, name='redacting'),
    path('my_progress.netlify.app', views.my_progress, name='my_progress'),
    path('contacts.netlify.app', views.contacts, name='contacts'),
    path('support.netlify.app', views.support, name='support'),
    path('team.netlify.app', views.team, name='team'),
    path('create_history.netlify.app', views.create_history, name='create_history'),
    path('crhis.netlify.app', views.crhis, name='crhis'),

]