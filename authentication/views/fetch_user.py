from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.helpers import validate_user_uid, decode_jwt_token
from authentication.services.user_services.user_services import UserServices


class FetchUserView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    def post(self, request: Request):
        user_id = decode_jwt_token(request=request)
        if validate_user_uid(uid=user_id).is_validated:
            requested_user_id = request.data.get("user_id")
            if not requested_user_id:
                raise ValueError("User ID is required.")
            user_details = UserServices().get_user_details_by_id(
                requested_user_id=requested_user_id, uid=user_id
            )
            return Response(
                data={
                    "message": "User details fetched successfully.",
                    "data": user_details.model_dump(),
                },
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            raise TokenError()
