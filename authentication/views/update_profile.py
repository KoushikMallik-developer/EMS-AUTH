from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

from authentication.export_types.request_data_types.update_user_profile import (
    UpdateUserProfileRequestType,
)
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.helpers import decode_jwt_token, validate_user_uid
from authentication.services.user_services.user_services import UserServices


class UpdateProfileView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    def post(self, request):
        user_id = decode_jwt_token(request=request)
        if validate_user_uid(uid=user_id).is_validated:
            user = UserServices().update_user_profile(
                uid=user_id,
                request_data=UpdateUserProfileRequestType(**request.data),
            )
            return Response(
                data={
                    "message": "User details updated Successfully.",
                    "data": user.model_dump(),
                },
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            raise TokenError()
