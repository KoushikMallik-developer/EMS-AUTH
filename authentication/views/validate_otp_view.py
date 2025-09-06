from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.export_types.request_data_types.verify_otp import (
    VerifyOTPRequestType,
)
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.user_services.user_services import UserServices


class ValidateOTPView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    def post(self, request: Request):
        token = UserServices().verify_user_with_otp(
            request_data=VerifyOTPRequestType(**request.data)
        )
        return Response(
            data={
                "token": token,
                "message": None,
            },
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
