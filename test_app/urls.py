# myapp/urls.py
from django.urls import path
from .views import display_active_patients, home, about, patients,skinTemp,stepCount,bp,heartRate,oxSat,pulse


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('active_patients/', patients, name='patients'),
    path('heartRate/', heartRate, name='heartRate'),
    path('bp/', bp, name='bp'),
    path('oxSat/', oxSat, name='oxSat'),
    path('pulse/', pulse, name='pulse'),
    path('stepCount/', stepCount, name='stepCount'),
    path('skinTemp/', skinTemp, name='skinTemp'),
    path('active_patients/', display_active_patients, name='active_patients'),
]


