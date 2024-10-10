from django.urls import path
from . import views

urlpatterns = [
    # passa uma var do tipo str pra view
    path('<str:name>', views.index, name="index"),
]