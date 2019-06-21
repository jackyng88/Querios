from rest_framework.response import Response
from rest_framework.views import APIView

from users.api.serializers import UserDisplaySerializer


class CurrentUserAPIView(APIView):
    # View class for the current authenticated user.

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)