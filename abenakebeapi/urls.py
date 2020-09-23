"""abenakebeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from abenakebe import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jokes/', views.JokeView.as_view()),
    path('jokes/image/', views.ImageJokeView.as_view()),
    path('jokes/meme/', views.MemeJokeView.as_view()),
    path('jokes/text/', views.TextJokeView.as_view()),
    path('jokes/all/', views.FeedView.as_view()),

    path('like/joke/', views.JokeLikeView.as_view()),
    path('like/image/', views.ImageLikeView.as_view()),
    path('like/meme/', views.MemeLikeView.as_view()),
    path('like/text/', views.TextLikeView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

