from django.urls import path
from .views import panel, displayForm

urlpatterns = [
    path('', panel, name='panel'),
    path('displayForm', displayForm, name="displayForm")
]
