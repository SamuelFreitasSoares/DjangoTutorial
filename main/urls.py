from django.urls import path
from . import views

urlpatterns = [
    # passa uma var do tipo str pra view
    path('<int:id>', views.index, name="index"),
]