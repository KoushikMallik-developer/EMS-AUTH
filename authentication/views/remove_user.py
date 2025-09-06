from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.auth_exceptions.user_exceptions import (
    UserNotFoundError,
    UserNotAuthenticatedError,
)
from authentication.models.user_models.user import User
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.helpers import (
    validate_user_email,
    decode_jwt_token,
    validate_user_uid,
)


class RemoveUserView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    def post(self, request):
        user_id = decode_jwt_token(request=request)
        if validate_user_uid(uid=user_id).is_validated:
            email = request.data.get("email")
            if not email:
                raise ValueError("Email is required.")
            if validate_user_email(email=email).is_validated:
                User.objects.get(email=email).delete()
                return Response(
                    data={
                        "message": "User removed Successfully.",
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
            else:
                raise UserNotFoundError()
        else:
            raise UserNotAuthenticatedError()
