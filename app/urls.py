from django.urls import path
from. import views

app_name='app'

urlpatterns=[
    path('home',views.home),
    path('new',views.new,name="new"),
    path('destiny',views.destiny,name="destiny"),
    path('about',views.about,name="about"),
    path('regi',views.regi,name="regi"),
]