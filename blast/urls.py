from django.urls import path

from blast.views import blastn

urlpatterns = [
    path('blastn/', blastn.as_view(), name='blastn')
 

]
