from django.urls import path

from .views import SignUpView, LoginUserView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', LoginUserView.as_view(), name='login')
]