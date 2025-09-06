from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.auth_exceptions.user_exceptions import (
    EmailNotSentError,
    UserAlreadyVerifiedError,
    UserNotFoundError,
)
from authentication.models.user_models.user import User
from authentication.services.definitions import DEFAULT_VERIFICATION_MESSAGE
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.helpers import validate_user_email
from authentication.services.otp_services.otp_services import OTPServices


class SendOTPView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    def post(self, request: Request):
        request_data = request.data
        email = request_data.get("email")
        if email and validate_user_email(email).is_validated:
            user = User.objects.get(email=email)
            if not user.is_active:
                response = OTPServices().send_otp_to_user(email)
                if response == "OK":
                    return Response(
                        data={
                            "message": DEFAULT_VERIFICATION_MESSAGE,
                        },
                        status=status.HTTP_200_OK,
                        content_type="application/json",
                    )
                else:
                    raise EmailNotSentError()
            else:
                raise UserAlreadyVerifiedError()
        else:
            raise UserNotFoundError()
