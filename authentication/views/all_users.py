from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.export_types.user_types.export_user import ExportUserList
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.user_services.user_services import UserServices


class AllUsersView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    def get(self, _):
        all_user_details = UserServices.get_all_users_service()
        if all_user_details and isinstance(all_user_details, ExportUserList):
            return Response(
                data={
                    "data": all_user_details.model_dump(),
                    "message": None,
                },
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            return Response(
                data={
                    "data": {"user_list": []},
                    "message": "No User found in database.",
                },
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
