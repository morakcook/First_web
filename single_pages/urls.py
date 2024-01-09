from django.urls import path
from .views import landing

urlpatterns = [
    path("", landing.as_view()),
    path("Is/Is_Is/", landing.as_view()),
    path("Is/Is_Sales/", landing.as_view()),
    path("Is/Is_Cos/", landing.as_view()),
    path("Is/Is_Exp/", landing.as_view()),
    path("Is/Is_Tax/", landing.as_view()),
    path("Is/Is_Netincome/", landing.as_view()),

    path("Fs/Fs_Iv/", landing.as_view()),
    path("Fs/Fs_Bs/", landing.as_view()),
    path("Fs/Fs_Note/", landing.as_view()),

    path("Em/Em_Status/", landing.as_view()),
    path("Em/Em_Compensation/", landing.as_view()),

    path("Bs/Bs_Contrac/", landing.as_view()),
    path("Bs/Bs_Artist/", landing.as_view()),
]