from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class CountView(APIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, site):
        # word = request.query_params.get('word')
        return Response({}, status=status.HTTP_200_OK)
