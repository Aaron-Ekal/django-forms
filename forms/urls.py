from . import views
from django.urls import path



urlpatterns = [
    path('', views.contact, name='contact'),
    # path('snippet', views.snippet_detail, name='snippet_detail')
]