from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.export_types.request_data_types.create_user import (
    CreateUserRequestType,
)
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.user_services.user_services import UserServices


class RegisterView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    def post(self, request: Request):
        result = UserServices.create_new_user_service(
            request_data=CreateUserRequestType(**request.data)
        )
        if result.get("successMessage"):
            return Response(
                data={
                    "message": result.get("successMessage"),
                },
                status=status.HTTP_201_CREATED,
                content_type="application/json",
            )
