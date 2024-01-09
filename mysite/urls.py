"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

#게시판 관련
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('Board/', include('single_pages.urls')),
    path('news/', include('data.urls')),

    #게시판 관련
    path('free_board/', include('free_board.urls')),
    path('markdownx/', include('markdownx.urls')),

    path('accounts/', include('allauth.urls')),
]

#게시판관련
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    # 미디어 파일을 서빙할 수 있도록 urlpatterns에 추가
)
