from collections import Counter

import requests
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from count_word_api.helpers.text import html_to_text, remove_punctuation


class CountView(APIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        word = request.query_params.get('word')
        url = request.query_params.get('url')
        response = requests.get(url)
        # convert html to text
        clean_text = html_to_text(response.text)
        # remove punctuation from text
        clean_text = remove_punctuation(clean_text)
        # create word_list
        word_list = Counter(clean_text.split())
        return Response({word: word_list[word]}, status=status.HTTP_200_OK)
