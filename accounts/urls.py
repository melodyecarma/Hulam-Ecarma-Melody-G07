from django.urls import path
from .views import HulamLoginView, HulamLogoutView, ProfileEditView, ProfileView, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", HulamLoginView.as_view(), name="login"),
    path("logout/", HulamLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
]