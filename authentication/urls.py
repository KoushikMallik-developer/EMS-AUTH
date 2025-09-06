from django.urls import path

from authentication.views.all_users import AllUsersView
from authentication.views.fetch_user import FetchUserView
from authentication.views.otp_view import SendOTPView
from authentication.views.password_reset import PasswordResetView
from authentication.views.refresh_token import RefreshTokenView
from authentication.views.register import RegisterView
from authentication.views.remove_user import RemoveUserView
from authentication.views.search_user import SearchUsersView
from authentication.views.sign_in import SignInView
from authentication.views.update_password import UpdatePasswordView
from authentication.views.update_profile import UpdateProfileView
from authentication.views.user_details import UserDetailView
from authentication.views.validate_otp_view import ValidateOTPView

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("sign-in", SignInView.as_view(), name="user-sign-in"),
    path("update-profile", UpdateProfileView.as_view(), name="Update-User-profile"),
    path("user-details", UserDetailView.as_view(), name="user-details"),
    path("all-users", AllUsersView.as_view(), name="All-Users"),
    path("remove-user", RemoveUserView.as_view(), name="Remove-User"),
    path("send-otp", SendOTPView.as_view(), name="send-otp"),
    path("verify-otp", ValidateOTPView.as_view(), name="verify-otp"),
    path(
        "reset-password",
        PasswordResetView.as_view(),
        name="send-reset-password-email",
    ),
    path("update-password", UpdatePasswordView.as_view(), name="Change-User-Password"),
    path("refresh-token", RefreshTokenView.as_view(), name="refresh-token"),
    path("search-users", SearchUsersView.as_view(), name="Search-Users"),
    path("user-details-by-id", FetchUserView.as_view(), name="Fetch-User"),
]
