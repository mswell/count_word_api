from collections import Counter

import requests
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from count_word_api.helpers.text import html_to_text, remove_punctuation
from .serializers import CountSerializer


class CountView(APIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        word = request.query_params.get('word')
        url = request.query_params.get('url')
        serializer = CountSerializer(data={"word": word, "url": url})
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            response = requests.get(url)
        except:
            return Response({"url": [
                "Site informado indisponível no momento"]},
                status=status.HTTP_400_BAD_REQUEST)

        # convert html to text
        clean_text = html_to_text(response.text)
        # remove punctuation from text
        clean_text = remove_punctuation(clean_text)
        # create word_list
        word_list = Counter(clean_text.split())
        return Response({word: word_list[word]}, status=status.HTTP_200_OK)
