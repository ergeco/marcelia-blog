from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post', views.create_post, name='create_post'),
    path('creating', views.creating, name='create'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('just_redact/<int:id>', views.just_redact, name='just_redact'),
    path('redacting/<int:id>', views.redacting, name='redacting'),
    path('my_progress', views.my_progress, name='my_progress'),
    path('contacts', views.contacts, name='contacts'),
    path('support', views.support, name='support'),
    path('create_history', views.create_history, name='create_history'),
    path('crhis', views.crhis, name='crhis'),

]