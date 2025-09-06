from django.urls import path

from authentication.views.register import RegisterView

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
]
