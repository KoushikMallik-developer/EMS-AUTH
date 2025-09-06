from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.auth_exceptions.user_exceptions import (
    UserNotFoundError,
)
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.user_services.user_services import UserServices


class PasswordResetView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    def post(self, request):
        email = request.data.get("email")
        if email:
            result = UserServices().reset_password(email=email)
            return Response(
                data={
                    "message": result.get("successMessage"),
                },
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            raise UserNotFoundError()
